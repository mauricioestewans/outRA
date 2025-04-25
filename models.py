from app import db

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)  # ex: 'image', 'video', '3D model'
    file_path = db.Column(db.String(255), nullable=False)
    
    def __init__(self, name, description, content_type, file_path):
        self.name = name
        self.description = description
        self.content_type = content_type
        self.file_path = file_path

class Projector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # ex: 'active', 'inactive'

class ARInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
    content = db.relationship('Content', backref=db.backref('ar_interactions', lazy=True))
    interaction_type = db.Column(db.String(100), nullable=False)  # ex: 'scan', 'click'
