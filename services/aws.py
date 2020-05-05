import boto3
from botocore import UNSIGNED
from botocore.client import Config
from config import Config as local_config


class AWS:
    def __init__(self):
        self.s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))

    def upload_file_to_s3(self, image, bucket_name, acl="public-read"):
        self.s3.upload_fileobj(
            image,
            bucket_name,
            image.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": image.content_type
            }
        )

        return f"{local_config.S3_LOCATION}/{image.filename}"


aws = AWS()
