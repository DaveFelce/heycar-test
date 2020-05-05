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
