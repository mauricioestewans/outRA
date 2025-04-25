from models import Projector
from app import db

class ProjectorService:
    @staticmethod
    def get_all_projectors():
        projectors = Projector.query.all()
        return [{'id': p.id, 'location': p.location, 'status': p.status} for p in projectors]

    @staticmethod
    def create_projector(location, status):
        new_projector = Projector(location=location, status=status)
        db.session.add(new_projector)
        db.session.commit()
        return {'id': new_projector.id, 'location': new_projector.location}
