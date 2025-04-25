class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///outdoor.db'  # Usando SQLite para testes, mas pode ser trocado para MySQL/PostgreSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
