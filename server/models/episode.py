from sqlalchemy.orm import relationship, validates
from server.app import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)

    appearances = relationship(
        'Appearance',
        back_populates='episode',
        cascade='all, delete-orphan'
    )

    @validates('date')
    def validate_date(self, key, date):
        """Ensures the date is present"""
        if not date:
            raise ValueError("Episode date is required.")
        return date

    @validates('number')
    def validate_number(self, key, number):
        """Ensures the episode number is present and positive"""
        if not number:
            raise ValueError("Episode number is required.")
        if not isinstance(number, int) or number <= 0:
            raise ValueError("Episode number must be a positive integer.")
        return number

    def __repr__(self):
        return f'<Episode {self.number} - {self.date}>'

    def to_dict(self, include_appearances=False):
        """
        Returns a dictionary representation of the episode.
        Optionally includes associated appearances.
        """
        episode_dict = {
            "id": self.id,
            "date": self.date.isoformat() if self.date else None,
            "number": self.number,
        }
        if include_appearances:
            episode_dict['appearances'] = [
                appearance.to_dict(include_guest=True) for appearance in self.appearances
            ]
        return episode_dict
