import os

import settings
from sqlalchemy.engine.url import URL

LOG_LEVEL = os.environ["LOG_LEVEL"]


class Config(object):
    SQLALCHEMY_DATABASE_URI = str(URL(**settings.DB)).replace('%', '%%')
    S3_BUCKET = os.environ.get('S3_BUCKET')
    S3_KEY = os.environ.get('S3_KEY')
    S3_SECRET = os.environ.get('S3_SECRET_ACCESS_KEY')
    S3_LOCATION = f"https://{S3_BUCKET}.s3.eu-west-2.amazonaws.com"
