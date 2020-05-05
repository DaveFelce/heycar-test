import logging
import os

LOG_LEVEL = os.environ["LOG_LEVEL"]


def get_logger(caller):
    # Setup logging
    logging.basicConfig(level=logging.getLevelName(LOG_LEVEL))
    return logging.getLogger(caller)
