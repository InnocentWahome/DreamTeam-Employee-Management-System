# config.py
import os

class Config(object):
    """
    Common configurations
    """
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_ECHO = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True



class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    SQLALCHEMY_ECHO = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}