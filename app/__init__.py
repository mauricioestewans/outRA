from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

db = SQLAlchemy()
ma = Marshmallow()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///outdoor.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    from app.routes import ContentResource, ProjectorResource, ARInteractionResource

    api.add_resource(ContentResource, '/api/content')
    api.add_resource(ProjectorResource, '/api/projector')
    api.add_resource(ARInteractionResource, '/api/ar')

    with app.app_context():
        db.create_all()

    return app
