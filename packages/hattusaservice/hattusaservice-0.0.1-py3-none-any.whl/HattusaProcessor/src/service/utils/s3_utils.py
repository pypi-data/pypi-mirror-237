from os import makedirs
from os.path import join, exists


from s3fs import S3FileSystem
from botocore.exceptions import EndpointConnectionError


def get_aws_access_settings(conf: dict, profile: str = "DEFAULT") -> dict:
    aws_access_settings = {
        "endpoint_url": conf[profile]["S3_ENDPOINT_URL"],
        "aws_access_key_id": conf[profile]["S3_ACCESS_KEY_ID"],
        "aws_secret_access_key": conf[profile]["S3_SECRET_ACCESS_KEY"],
        "region_name": conf[profile]["S3_REGION_NAME"],
    }

    return aws_access_settings


class HattusaS3FileSystem(S3FileSystem):
    def __init__(self, *args, **kwargs):
        self.default_bucket: str = None
        self.local_temp: str = None
        super(HattusaS3FileSystem, self).__init__(*args, **kwargs)


def get_s3fs(conf: dict, profile: str = "DEFAULT", logger=None) -> HattusaS3FileSystem:
    kwargs = get_aws_access_settings(conf, profile="DEFAULT")

    try:
        fs = HattusaS3FileSystem(anon=False, client_kwargs=kwargs)
        if fs is not None:
            try:
                fs.ls("/")
                return fs
            except FileNotFoundError:
                return fs
        else:
            logger.error("FS object is None")
    except ValueError as e:
        logger.error(f"{str(e)}")
    except PermissionError:
        logger.error("S3 Authentication Failed")
    except EndpointConnectionError:
        logger.error("Can't Connect to S3 Endpoint")
    except Exception as e:
        logger.error(f"Undefined Error: {str(e)}")


class HattusaS3Object:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.connections = {}  # Dictionary to store S3Fs instances

        self._create_connections()

    def _get_profiles(self):
        return self.config.keys()

    def _create_connections(self):
        for profile in self._get_profiles():
            fs: HattusaS3FileSystem = get_s3fs(self.config, profile, self.logger)
            fs.default_bucket = self.config[profile]["S3_DEFAULT_BUCKET"]
            fs.local_temp = self.config[profile]["S3_LOCAL_TEMP_DIR"]
            self.connections[profile.lower()] = fs

    def _get_profile(self, connection_name):
        if connection_name in self.connections:
            return self.connections[connection_name]
        else:
            raise ValueError(
                f"Connection '{connection_name}' not found in the configuration."
            )

    def __getattr__(self, name):
        if name in self.connections:
            return self._get_profile(name)
        else:
            raise AttributeError(f"'S3Storage' object has no attribute '{name}'")
