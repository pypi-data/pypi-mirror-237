from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


from .redis_utils import generate_redis_conf


def init_scheduler():
    """Short summary.

    Returns
    -------
    BackgroundScheduler
        Description of returned object.

    """
    global scheduler
    if not scheduler:
        jobstores = {
            "default": RedisJobStore(
                jobs_key=f"scheduler_{CLUSTER}_jobs",
                run_times_key=f"scheduler_{CLUSTER}_runtimes",
                host=REDIS_HOST,
                port=REDIS_PORT,
                db=REDIS_DB,
                password=REDIS_PW,
            )
        }
        executors = {"default": ProcessPoolExecutor(5)}
        job_defaults = {"coalesce": False, "max_instances": 3}

        scheduler = BackgroundScheduler(
            jobstores=jobstores,
            executors=executors,
            job_defaults=job_defaults,
            timezone=utc,
        )

    return scheduler


class HattusaSchedulert:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.scheduler = {}  # Dictionary to store S3Fs instances

        def _get_store(self, type="redis") -> dict:
            cluster: str = self.config["REDIS_STREAM"]["REDIS_STREAM_CONSUMER_GROUP"]
            redis_conf = generate_redis_conf(self.config)
            jobstores = {
                "default": RedisJobStore(
                    jobs_key=f"scheduler_{cluster}_jobs",
                    run_times_key=f"scheduler_{cluster}_runtimes",
                    **redis_conf,
                )
            }

            return jobstores

        def _create_scheduler(self):
            jobstores = self._get_store()
            executors = {"default": ProcessPoolExecutor(5)}
            job_defaults = {"coalesce": False, "max_instances": 3}

            scheduler = BackgroundScheduler(
                jobstores=jobstores,
                executors=executors,
                job_defaults=job_defaults,
                timezone=utc,
            )

            self.scheduler = scheduler
