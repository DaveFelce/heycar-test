import boto3
from botocore import UNSIGNED
from botocore.client import Config
from config import Config as local_config


class AWS:
    """
    Helper class for all thing AWS related
    """
    def __init__(self):
        self.s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))

    def upload_file_to_s3(self, image, bucket_name: str, acl="public-read") -> str:
        """

        :param image: The uploaded image object
        :param bucket_name: S3 bucket name
        :param acl:
        :return: The URL for the image on S3
        """
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
