# -*- coding: utf-8 -*-

class Config():
    SECRET_KEY = 'SECRET KEY'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'

class TestingConfig(Config):
    pass