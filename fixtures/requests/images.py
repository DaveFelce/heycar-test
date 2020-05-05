import io

import pytest
from server import flask_app


@pytest.fixture(scope="session")
def get_image():
    def _get_image(image_id: str):

        query_string = f"?image_id={image_id}"
        url = f"/image{query_string}"
        response = flask_app.test_client().get(url)

        return response

    return _get_image


@pytest.fixture(scope="session")
def create_image():
    def _create_image(name):
        req_body = {"name": name}
        req_body["image"] = (io.BytesIO(b"this is a test"), "test_image.jpg")

        url = f"/image"
        response = flask_app.test_client().post(url, data=req_body)

        return response

    return _create_image
