import pytest
from services.db import db


@pytest.fixture(scope="session")
def db_fixture():

    yield db


@pytest.fixture(scope="function")
def seed_image(db_fixture):
    image_ids = []

    # TODO: normally would use factories to populate
    def _seed_image(image_id, name, image_url):
        # Update the image table
        db_fixture.add_image_record(image_id=image_id, name=name, image_url=image_url)
        image_ids.append(image_id)
        return image_id

    yield _seed_image

    for image_id in image_ids:
        db.delete_image_record(image_id)
