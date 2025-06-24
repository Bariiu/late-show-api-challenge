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

    @validates('guest_id')
    def validate_guest_id(self, key, guest_id):
        """Ensures guest_id is present"""
        if not guest_id:
            raise ValueError("Guest ID is required.")
        return guest_id

    @validates('episode_id')
    def validate_episode_id(self, key, episode_id):
        """Ensures episode_id is present"""
        if not episode_id:
            raise ValueError("Episode ID is required.")
        return episode_id

    def __repr__(self):
        return f'<Appearance {self.id} | Rating: {self.rating}>'

    def to_dict(self, include_guest=False, include_episode=False):
        """
        Returns a dictionary representation of the appearance.
        Optionally includes associated guest and episode data.
        """
        appearance_dict = {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id,
        }
        if include_guest and self.guest:
            appearance_dict['guest'] = self.guest.to_dict()
        if include_episode and self.episode:
            appearance_dict['episode'] = {
                "id": self.episode.id,
                "date": self.episode.date.isoformat() if self.episode.date else None,
                "number": self.episode.number,
            }
        return appearance_dict
