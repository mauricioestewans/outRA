from models import ARInteraction
from app import db

class ARService:
    @staticmethod
    def create_ar_interaction(content_id, interaction_type):
        new_interaction = ARInteraction(content_id=content_id, interaction_type=interaction_type)
        db.session.add(new_interaction)
        db.session.commit()
        return {'id': new_interaction.id, 'interaction_type': new_interaction.interaction_type}
