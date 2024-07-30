import os
class Config:
    # SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    EUREKA_SERVER = os.environ.get('EUREKA_SERVER', 'http://localhost:8761/eureka/')
    APP_NAME = os.environ.get('APP_NAME', 'your-flask-app')
    INSTANCE_PORT = int(os.environ.get('INSTANCE_PORT', 9000))
    INSTANCE_IP = os.environ.get('INSTANCE_IP', '127.0.0.1')
    INSTANCE_HOST_NAME = os.environ.get('INSTANCE_HOST_NAME', 'localhost')