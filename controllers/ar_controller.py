from flask_restful import Resource
from flask import request
from services.ar_service import ARService

class ARController(Resource):
    def post(self):
        data = request.get_json()
        interaction = ARService.create_ar_interaction(data['content_id'], data['interaction_type'])
        return {'message': 'AR interaction created!', 'interaction': interaction}, 201
