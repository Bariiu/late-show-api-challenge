from sqlalchemy.orm import relationship, validates
from server.app import db

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100))

    appearances = relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')

    @validates('name')
    def validate_name(self, key, name):
        """Ensures the guest name is present"""
        if not name:
            raise ValueError("Guest name is required.")
        return name

    def __repr__(self):
        return f'<Guest {self.name}>'

    def to_dict(self):
        """Returns a dictionary representation of the guest"""
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
        }
