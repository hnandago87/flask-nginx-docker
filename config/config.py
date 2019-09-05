from pathlib import Path

class Config:
    __ROOT_PATH = Path(__file__).resolve().parent
    DEBUG = False
    TESTING = False
    SECRET_KEY = b'\x94\xbf\xa5\x9e\x14\x06\x115\xc3N\xb8oi\xcay(' # Change to a new KEY! 
    ROOT_PATH = __ROOT_PATH

class ProductionConfig(Config):
    DATABASE_URI = '' # MySQL, PostgreSQL, MariaDB, etc.

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    ENV = 'development'
    HOST= '127.0.0.1'
    PORT= 5000

class TestingConfig(Config):
    TESTING = True
