class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://lateshow_user:securepassword@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-jwt-key"
