from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from config.application import config
from app.http.controllers.api.PredictionController import PredictionController

# -------------------------------------------------------------------------
# Extension Objects
# -------------------------------------------------------------------------
#
# Initialize extensions accessible to any part of our app
api = Api()


def create_app() -> Flask:
    """
    Create The Application
    The first thing we will do is create a new application instance
    which serves as the "glue" for all the components of the api.
    :return: Flask
    """
    app = Flask(__name__)

    app.config.from_mapping(
        ENV=config["env"], DEBUG=config["debug"], SECRET_KEY=config["key"]
    )

    CORS(app, origins=config["origins"])

    # Initialize Extensions
    api.init_app(app)

    with app.app_context():
        # Register resources
        api.add_resource(PredictionController, "/prediction")

    return app


__version__ = "0.1.0"
