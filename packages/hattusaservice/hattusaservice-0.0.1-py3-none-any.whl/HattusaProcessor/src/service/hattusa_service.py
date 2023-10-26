import multiprocessing
import threading
import logging
import logging.config
import time

import orjson as json
import redis

from reactivex.scheduler import ThreadPoolScheduler
from reactivex.subject import Subject

from .utils import process_config, get_connection, get_s3fs, HattusaS3Object


class HattusaProcessor:
    def __init__(self):
        self.config = {}
        self.redis = None
        self.storage: HattusaS3Object = None
        self.logger = None
        self.scheduler = None
        self.rx_subject = Subject()
        self.leader: bool = False
        self.working: bool = False
        self.leader_lock = threading.Lock()
        self.leader_lock_key = None
        self.leader_lock_ttl = 5  # Lock expiration time in seconds
        self.leader_event = threading.Event()

        optimal_thread_count = multiprocessing.cpu_count()
        self.rx_scheduler = ThreadPoolScheduler(optimal_thread_count)

        """
        self.leader_key = f"{self.config['redis']['stream']}_leader"
        self.leader_lock_ttl = 30  # Lock expiration time in seconds
        self.logger = self.setup_logging()
        """

    def set_config(self, config_file="config.json", update=True):
        config = process_config(config_file, update)
        self.config = config
        return config

    def setup_logging(self, name="hattusa-processor") -> logging.Logger:
        log_level = self.config.get("HATTUSA_LOGLEVEL", "INFO")
        service_name = self.config.get("SERVICE_NAME", "hattusa-processor")
        instance_id = self.config.get("INSTANCE_ID", "")

        l_format = (
            f"%(asctime)s - [%(levelname)s] [Service: {service_name}] "
            f"[Worker: {instance_id}]: [%(funcName)s]: %(message)s"
        )

        LOGGING_CONFIG = {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "standard": {
                    "format": l_format,
                },
            },
            "handlers": {
                "default": {
                    "level": log_level,
                    "formatter": "standard",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",  # Default is stderr
                },
                "file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "INFO",
                    "formatter": "standard",
                    "filename": "service.log",
                    "mode": "a",
                    "maxBytes": 10485760,
                    "backupCount": 5,
                },
            },
            "loggers": {
                "": {  # root logger
                    "handlers": ["default", "file"],
                    "level": "DEBUG",
                    "propagate": False,
                }
            },
        }

        logging.config.dictConfig(LOGGING_CONFIG)
        logger = logging.getLogger(name)

        self.logger = logger

        return logger

    def connect_to_redis(self):
        try:
            ping = self.redis.ping()
            if ping:
                return None
        except Exception as exc:
            log_txt = "No active Redis connection"
            self.logger.info(log_txt)

        retries = 0

        while True:
            try:
                log_txt = "Trying to connect to Redis"
                self.logger.info(log_txt)
                self.redis = get_connection(self.config)
                self.redis.ping()  # Test the connection
                self.logger.info("Connected to Redis")
                break
            except (redis.ConnectionError, redis.RedisError) as e:
                retries += 1
                self.logger.error(f"Error connecting to Redis: {e}")
                delay = min(2**retries, 30)
                self.logger.warning(f"Retrying in {delay} seconds...")
                time.sleep(delay)

    def get_redis(self):
        try:
            ping = self.redis.ping()
            if ping:
                return self.redis
            else:
                self.connect_to_redis()
                return self.get_redis()
        except AttributeError as aexc:
            log_txt = "No active Redis connection."
            self.logger.warning(log_txt)
            self.connect_to_redis()
            return self.get_redis()

    def setup_storage(self):
        storage: HattusaS3Object = HattusaS3Object(self.config["S3"], self.logger)
        self.storage = storage

    def init_processor(self):
        if not self.config:
            return None

        self.setup_logging()
        self.logger.info("Configuration is loaded")

        self.connect_to_redis()
        self.logger.info("Redis connection is established")

        if self.config["STORAGE_ENABLED"]:
            self.setup_storage()

    def get_lock_key(self) -> str:
        if not self.leader_lock_key:
            consumer_group: str = self.config["REDIS_STREAM"][
                "REDIS_STREAM_CONSUMER_GROUP"
            ]
            lock_key: str = f"{consumer_group}"
            self.leader_lock_key = lock_key

        return self.leader_lock_key

    def acquire_leader_lock(self):
        lock_key: str = self.get_lock_key()
        lock_value: str = self.config["INSTANCE_ID"]
        ttl: int = self.leader_lock_ttl
        with self.leader_lock:
            acquired = self.redis.set(lock_key, lock_value, ex=ttl, nx=True)
            self.leader = acquired
            if acquired:
                self.logger.info("Acquired leader lock")
                return True
            else:
                self.logger.info(
                    "Failed to acquire leader lock, sleeping and retrying..."
                )
                time.sleep(self.leader_lock_ttl)

    def release_leader_lock(self):
        self.redis.delete(self.leader_key)
        self.leader_lock = False
        self.logger.info("Released leader lock")

    def extend_leader_lock(self):
        if self.leader:
            lock_key: str = self.get_lock_key()
            while True:
                time.sleep(
                    self.leader_lock_ttl // 2
                )  # Extend the lock every half of the TTL
                with self.leader_lock:
                    self.redis.expire(lock_key, self.leader_lock_ttl)
                    self.logger.info("Extended leader lock")

    def run_for_leader(self):
        if self.leader:
            self.extend_leader_lock()
        else:
            self.acquire_leader_lock()
            self.run_for_leader()

    def am_I_leader(self):
        while True:
            self.logger.info(f"Am I a leader? {self.leader}")
            time.sleep(10)

    def consume_messages(self):
        self.connect_to_redis()

        while True:
            if self.acquire_leader_lock():
                try:
                    message = self.redis.xread(
                        {self.config["redis"]["stream"]: "0"}, count=1
                    )
                    self.message_queue.put(message)
                except (redis.ConnectionError, redis.RedisError) as e:
                    self.logger.error(f"Error reading from Redis stream: {e}")
                finally:
                    self.release_leader_lock()

    def process_messages(self):
        while True:
            message = self.message_queue.get()
            self.logger.info(f"Received message: {message}")

    def start_server(self):
        self.logger.info("Starting server...")
        threading.Thread(target=self.run_for_leader).start()
        self.logger.info("Starting server 2...")
        threading.Thread(target=self.am_I_leader).start()
        # threading.Thread(target=self.extend_leader_lock).start()
        # threading.Thread(target=self.process_messages).start()

    def stop_server(self):
        self.logger.info("Stopping server...")
        if self.redis:
            self.redis.close()
            self.logger.info("Redis connection closed")
            self.release_leader_lock()  # Ensure that the leader lock is released on shutdown
