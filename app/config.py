from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')

    UPLOAD_FOLDER = 'app/static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 #2MB

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}