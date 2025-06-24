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