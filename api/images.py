import uuid

import utils
from config import Config
from flask import g, request

logger = utils.get_logger(__name__)


def post():
    # Create new image id
    image_id = str(uuid.uuid4())

    name = request.form.get("name")
    image = request.files.get("image")

    if image:
        try:
            image_filename = g.aws.upload_file_to_s3(
                image=image,
                bucket_name=Config.S3_BUCKET
            )
        except Exception:
            msg = "Error uploading image to S3"
            logger.exception(msg)
            return msg, 500
    else:
        return "Please upload an image file", 400

    # Update the image table
    # dal_authors.add_author(
    #     name, info, image_filename, id=id, institution_id=institution_id
    # )

    data = {"image_id": image_id}

    # Done
    return data, 201


def get():
    thing = 1

    return "Get is alive", 200
