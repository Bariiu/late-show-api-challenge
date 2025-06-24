import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URI", "postgresql://<user>:<password>@localhost:5432/late_show_db"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "your_super_secret_jwt_key")

JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)

JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

print(f"Database URI: {SQLALCHEMY_DATABASE_URI}")
