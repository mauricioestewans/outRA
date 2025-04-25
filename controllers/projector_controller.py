from flask_restful import Resource
from flask import request
from services.projector_service import ProjectorService

class ProjectorController(Resource):
    def get(self):
        projectors = ProjectorService.get_all_projectors()
        return {'projectors': projectors}, 200

    def post(self):
        data = request.get_json()
        projector = ProjectorService.create_projector(data['location'], data['status'])
        return {'message': 'Projector created successfully!', 'projector': projector}, 201
