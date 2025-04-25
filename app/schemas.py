from app import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import Content, Projector, ARInteraction

class ContentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Content
        load_instance = True

class ProjectorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Projector
        load_instance = True

class ARInteractionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ARInteraction
        load_instance = True
