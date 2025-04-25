from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from pathlib import Path
import os
import logging

# Inicializa a app
app = Flask(__name__)
base_dir = Path(os.getcwd())
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{base_dir / "outdoor.db"}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração de log básico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

# Modelos
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    content_type = db.Column(db.String(50))
    file_path = db.Column(db.String(200))

class Projector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50))

class ARInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
    interaction_type = db.Column(db.String(100))

# Schemas
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

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)
projector_schema = ProjectorSchema()
projectors_schema = ProjectorSchema(many=True)
ar_schema = ARInteractionSchema()
ars_schema = ARInteractionSchema(many=True)

# Recursos
class ContentResource(Resource):
    def get(self):
        contents = Content.query.all()
        return contents_schema.dump(contents), 200

    def post(self):
        data = request.get_json()
        new_content = Content(
            name=data['name'],
            description=data['description'],
            content_type=data['content_type'],
            file_path=data['file_path']
        )
        db.session.add(new_content)
        db.session.commit()
        return content_schema.dump(new_content), 201

class ProjectorResource(Resource):
    def get(self):
        projectors = Projector.query.all()
        return projectors_schema.dump(projectors), 200

    def post(self):
        data = request.get_json()
        new_projector = Projector(
            location=data['location'],
            status=data['status']
        )
        db.session.add(new_projector)
        db.session.commit()
        return projector_schema.dump(new_projector), 201

class ARInteractionResource(Resource):
    def get(self):
        interactions = ARInteraction.query.all()
        return ars_schema.dump(interactions), 200

    def post(self):
        data = request.get_json()
        new_ar = ARInteraction(
            content_id=data['content_id'],
            interaction_type=data['interaction_type']
        )
        db.session.add(new_ar)
        db.session.commit()
        return ar_schema.dump(new_ar), 201

# Rota raiz (página inicial)
@app.route('/')
def home():
    return "Bem-vindo à API de Outdoor! Use as rotas /api/content, /api/projector ou /api/ar."

# Rotas da API
api.add_resource(ContentResource, '/api/content')
api.add_resource(ProjectorResource, '/api/projector')
api.add_resource(ARInteractionResource, '/api/ar')

# Inicializa o banco de dados
with app.app_context():
    db.create_all()

# Execução
# ... (código anterior permanece igual)

# Execução
if __name__ == '__main__':
    try:
        logger.info("Iniciando o servidor...")
        # Desativa o reloader e threading explicitamente
        app.run(
            debug=False,          # Debug DESLIGADO
            use_reloader=False,  # Garante que o reloader está desativado
            threaded=False       # Evita o uso de threads
        )
    except Exception as e:
        logger.error(f"Erro ao iniciar o servidor: {e}")