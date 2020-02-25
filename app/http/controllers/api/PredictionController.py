from flask_restful import Resource


class PredictionController(Resource):
    def get(self, data=None):
        return data
