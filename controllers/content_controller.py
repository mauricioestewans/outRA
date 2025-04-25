from flask_restful import Resource
from flask import request
from models import Content
from services.content_service import ContentService

class ContentController(Resource):
    def get(self):
        content = ContentService.get_all_content()
        return {'content': content}, 200

    def post(self):
        data = request.get_json()
        content = ContentService.create_content(data['name'], data['description'], data['content_type'], data['file_path'])
        return {'message': 'Content created successfully!', 'content': content}, 201
