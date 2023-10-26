import redis


def generate_redis_conf(conf: dict) -> dict:
    redis_conf = {
        "host": conf["REDIS"]["REDIS_HOST"],
        "port": conf["REDIS"]["REDIS_PORT"],
        "db": conf["REDIS"]["REDIS_DB"],
        "password": conf["REDIS"]["REDIS_PASSWORD"],
    }

    return redis_conf


def get_connection(conf: dict) -> redis.Redis:
    redis_conf = generate_redis_conf(conf)

    pool = redis.ConnectionPool(**redis_conf)
    conn = redis.Redis.from_pool(pool)

    return conn
