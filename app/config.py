from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_USER = os.getenv('MYSQL_USER')
    DB_PASS = os.getenv('MYSQL_PASSWORD')
    DB_HOST = os.getenv('MYSQL_HOST')
    DB_PORT = os.getenv('MYSQL_PORT', 3306)
    DB_NAME = os.getenv('MYSQL_DB')

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = 'app/static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
