from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from config.application import config
from app.http.controllers.api.PredictionController import PredictionController

app = Flask(__name__)
app.config.from_mapping(
    ENV=config['env'],
    DEBUG=config['debug'],
    SECRET_KEY=config['key']
)

CORS(app, origins=config['origins'])

api = Api(app)
api.add_resource(PredictionController, '/prediction')

__version__ = "0.1"
