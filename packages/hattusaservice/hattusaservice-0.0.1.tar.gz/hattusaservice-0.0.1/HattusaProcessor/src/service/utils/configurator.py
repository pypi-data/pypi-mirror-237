import os
import orjson

from .generator_utils import generate_string


def open_config(config_file: str) -> dict:
    with open(config_file, "rb") as f:
        conf = orjson.loads(f.read())
    return conf


def check_env(conf: dict) -> dict:
    for key in conf:
        env_value = os.environ.get(key, None)
        if env_value:
            conf[key] = env_value

    keys = ["REDIS", "REDIS_STREAM"]

    for k in keys:
        for key in conf[k]:
            env_value = os.environ.get(key, None)
            if env_value:
                conf[k][key] = env_value

    if conf["STORAGE_ENABLED"]:
        for key in conf["S3"]["DEFAULT"]:
            env_value = os.environ.get(key, None)
            if env_value:
                conf["S3"]["DEFAULT"][key] = env_value

    return conf


def check_config(conf: dict):
    updated_flag = False

    if not conf["INSTANCE_ID"]:
        updated_flag = True
        generated_id = generate_string()
        conf["INSTANCE_ID"] = generated_id

    if "_" in conf["SERVICE_NAME"]:
        updated_flag = True
        conf["SERVICE_NAME"] = conf["SERVICE_NAME"].replace("_", "-")

    if not conf["REDIS_STREAM"]["REDIS_STREAM_GROUP_NAME"]:
        conf["REDIS_STREAM"]["REDIS_STREAM_GROUP_NAME"] = "default"

    if "_" in conf["REDIS_STREAM"]["REDIS_STREAM_GROUP_NAME"]:
        updated_flag = True
        conf["REDIS_STREAM"]["REDIS_STREAM_GROUP_NAME"] = conf["REDIS_STREAM"][
            "REDIS_STREAM_GROUP_NAME"
        ].replace("_", "-")

    if not conf["REDIS_STREAM"]["REDIS_STREAM_GROUP_PREFIX"]:
        updated_flag = True
        group_prefix: str = f'{conf["SERVICE_NAME"]}'
        conf["REDIS_STREAM"]["REDIS_STREAM_GROUP_PREFIX"] = group_prefix

    consumer_group: str = conf["REDIS_STREAM"]["REDIS_STREAM_CONSUMER_GROUP"]

    if consumer_group:
        if "_" in consumer_group:
            updated_flag = True
            consumer_group = consumer_group.replace("_", "-")

    else:
        updated_flag = True
        group_prefix: str = conf["REDIS_STREAM"]["REDIS_STREAM_GROUP_PREFIX"]
        group_name: str = conf["REDIS_STREAM"]["REDIS_STREAM_GROUP_NAME"]
        consumer_group = f"consumergroup_{group_prefix}-{group_name}"

    conf["REDIS_STREAM"]["REDIS_STREAM_CONSUMER_GROUP"] = consumer_group
    return conf, updated_flag


def update_config(conf: dict, config_file: str):
    opts = orjson.OPT_INDENT_2 | orjson.OPT_APPEND_NEWLINE
    with open(config_file, "wb") as f:
        f.write(orjson.dumps(conf, option=opts))


def process_config(config_file, update=False):
    updated_flag = False
    conf = open_config(config_file)
    conf = check_env(conf)
    conf, updated_flag = check_config(conf)

    if update and updated_flag:
        update_config(conf, config_file)

    return conf
