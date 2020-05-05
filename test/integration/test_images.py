from fixtures.requests.images import create_image, get_image


# TODO: Huge caveat!! This would normally be done against a separate, temporary test DB !!
# TODO: There would normally be a LOT more tests, these are just basic examples of pytest/fixtures
class TestImage:
    def test_get_image(
        self,
        seed_image,
        get_image,
    ):
        """
        Test the GET request

        :param db_session: DB helper fixture
        :param get_image: Request fixture for /image
        """

        # GIVEN
        # idea = seed_idea(user_student[0].id, idea_status_published)
        image_id = "7695667e-ce87-4ce1-929c-a1cbd398b999"
        name = "testname"
        image_url = "https://heycar-davidfelce-test.s3.eu-west-2.amazonaws.com/ELRFtJyXYAAdddd.jpg"
        seed_image(image_id=image_id, name=name, image_url=image_url)

        # WHEN
        response = get_image(
            image_id=image_id,
        )
        json_data = response.get_json()["data"]

        # THEN
        assert json_data["image_id"] == image_id
        assert json_data["image_url"] == image_url
        assert json_data["name"] == name

    # TODO: Normally would mock all of this - anything past the app's boundary
    def test_create_image(
        self,
        create_image
    ):
        """
        Test POST of image

        :param create_image: create image request fixture
        :return:
        """
        # GIVEN
        name = "my_cool_picture.jpeg"

        # WHEN
        response = create_image(
            name=name,
        )

        # THEN
        assert response.status_code == 201
