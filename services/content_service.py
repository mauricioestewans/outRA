from models import Content
from app import db

class ContentService:
    @staticmethod
    def get_all_content():
        content_list = Content.query.all()
        return [{'id': c.id, 'name': c.name, 'description': c.description} for c in content_list]

    @staticmethod
    def create_content(name, description, content_type, file_path):
        new_content = Content(name, description, content_type, file_path)
        db.session.add(new_content)
        db.session.commit()
        return {'id': new_content.id, 'name': new_content.name}
