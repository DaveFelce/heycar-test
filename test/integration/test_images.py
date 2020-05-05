from fixtures.requests.images import get_image


class TestImage:
    def test_get_image(
        self,
        db_session,
        get_image,
    ):
        """

        :param db_session: DB helper fixture
        :param get_image: Request fixture for /image
        """

        # GIVEN
        # idea = seed_idea(user_student[0].id, idea_status_published)

        # WHEN
        response = get_image(
            image_id="7695667e-ce87-4ce1-929c-a1cbd398b181",
        )
        json_data = response.get_json()["data"]

        # THEN
        assert json_data["image_id"] == "7695667e-ce87-4ce1-929c-a1cbd398b181"
        assert json_data["image_url"] == "https://heycar-davidfelce-test.s3.eu-west-2.amazonaws.com/ELRFtJyXYAAtmbw.jpg"
        assert json_data["name"] == "Lewes bridge"
