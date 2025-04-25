from flask_restful import Resource, request
from app import db
from app.models import Content, Projector, ARInteraction
from app.schemas import ContentSchema, ProjectorSchema, ARInteractionSchema

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)
projector_schema = ProjectorSchema()
projectors_schema = ProjectorSchema(many=True)
ar_schema = ARInteractionSchema()
ars_schema = ARInteractionSchema(many=True)

class ContentResource(Resource):
    def get(self):
        contents = Content.query.all()
        return contents_schema.dump(contents), 200

    def post(self):
        data = request.get_json()
        new_content = Content(**data)
        db.session.add(new_content)
        db.session.commit()
        return content_schema.dump(new_content), 201

class ProjectorResource(Resource):
    def get(self):
        projectors = Projector.query.all()
        return projectors_schema.dump(projectors), 200

    def post(self):
        data = request.get_json()
        new_projector = Projector(**data)
        db.session.add(new_projector)
        db.session.commit()
        return projector_schema.dump(new_projector), 201

class ARInteractionResource(Resource):
    def get(self):
        interactions = ARInteraction.query.all()
        return ars_schema.dump(interactions), 200

    def post(self):
        data = request.get_json()
        new_ar = ARInteraction(**data)
        db.session.add(new_ar)
        db.session.commit()
        return ar_schema.dump(new_ar), 201
