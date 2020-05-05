import utils
from flask import g
from services.db import db


logger = utils.get_logger(__name__)


def post():
    return "Alive!", 200


def get():
    thing = 1

    return "Get is alive", 200
