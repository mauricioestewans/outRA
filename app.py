from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from config import Config

# Iniciando o app
app = Flask(__name__)
app.config.from_object(Config)

# Iniciando banco de dados e Marshmallow (para serializar)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Iniciando API
api = Api(app)

# Importando controladores
from controllers.content_controller import ContentController
from controllers.projector_controller import ProjectorController
from controllers.ar_controller import ARController

# Definindo as rotas
api.add_resource(ContentController, '/content')
api.add_resource(ProjectorController, '/projector')
api.add_resource(ARController, '/ar')

if __name__ == '__main__':
    app.run(debug=True)
