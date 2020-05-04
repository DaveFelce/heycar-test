import logging
import os

import settings
from sqlalchemy.engine.url import URL

LOG_LEVEL = os.environ["LOG_LEVEL"]


class Config(object):
    SQLALCHEMY_DATABASE_URI = str(URL(**settings.DB)).replace('%', '%%')

    @staticmethod
    def get_logger(caller):
        # Setup logging
        logging.basicConfig(level=logging.getLevelName(LOG_LEVEL))
        return logging.getLogger(caller)
