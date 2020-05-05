import os

import connexion
import utils
from flask import g, redirect
from services.aws import aws
from services.db import db

env = os.environ.get("ENV")

app = connexion.FlaskApp(__name__, specification_dir="./")
# Read the swagger.yml file to configure the endpoints
options = {"strict_validation": True, "validate_responses": True}
app.add_api("openapi.yml", options=options)

flask_app = app.app

logger = utils.get_logger(__name__)


# Grab a DB connection
@flask_app.before_request
def get_db_connection():
    g.db = db
    g.aws = aws


# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    redirect to the UI
    """

    return redirect("/ui", code=302)


if __name__ == "__main__":
    # Port needed for development
    app.run(debug=True, host=os.environ.get('HOST', '0.0.0.0'), port=5000)
