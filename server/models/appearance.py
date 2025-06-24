from sqlalchemy.orm import relationship, validates
from sqlalchemy.schema import UniqueConstraint
from server.app import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    guest = relationship('Guest', back_populates='appearances')
    episode = relationship('Episode', back_populates='appearances')

    __table_args__ = (UniqueConstraint('guest_id', 'episode_id', name='_guest_episode_uc'),)

    @validates('rating')
    def validate_rating(self, key, rating):
        """Ensures the rating is between 1 and 5 (inclusive)"""
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        return rating