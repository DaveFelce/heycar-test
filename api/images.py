import uuid

import utils
from config import Config
from flask import g, request

logger = utils.get_logger(__name__)


def post():
    """
    Upload a new image
    :return: Response with data
    """
    # Create new image id
    image_id = str(uuid.uuid4())

    name = request.form.get("name")
    image = request.files.get("image")

    if image:
        try:
            image_url = g.aws.upload_file_to_s3(
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
    g.db.add_image_record(image_id=image_id, name=name, image_url=image_url)

    data = {"image_id": image_id}

    # Done
    return {"data": data}, 201


def get():
    """
    Retrieve an image's details from the DB
    :return: Response with image data
    """
    image_id = request.args.get("image_id")

    if image_id:
        # Update the image table
        name, image_url = g.db.get_image_record(image_id=image_id)
    else:
        return "Please provide an image id", 400

    data = {"image_id": image_id, "name": name, "image_url": image_url}

    # Done
    return {"data": data}, 200
