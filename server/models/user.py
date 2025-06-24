from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

from server.app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _password_hash = db.Column(db.String(128), nullable=False)

    @hybrid_property
    def password_hash(self):
        """Prevents direct access to the password hash"""
        raise AttributeError('Password hashes cannot be read.')

    @password_hash.setter
    def password_hash(self, password):
        """Hashes the password before storing it"""
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the provided password against the stored hash"""
        return check_password_hash(self._password_hash, password)

    @validates('username')
    def validate_username(self, key, username):
        """Ensures the username is present and unique"""
        if not username:
            raise ValueError("Username is required.")
        if not self.id and User.query.filter_by(username=username).first():
            raise ValueError("Username must be unique.")
        return username

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        """Returns a dictionary representation of the user (excluding password hash)"""
        return {
            "id": self.id,
            "username": self.username,
        }
