import os

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    #SQLALCHEMY_DATABASE_URI = 'postgresql://stock_user:password@127.0.0.1:5432/stock_database'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///produits_db.db'

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tests/randomCityDbTest.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False