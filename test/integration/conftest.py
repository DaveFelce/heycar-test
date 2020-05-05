import os

import pytest
from services.db import db


@pytest.fixture(scope="session")
def db_session():

    yield db
