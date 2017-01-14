# -*- coding: utf-8 -*-

class Config():
    SECRET_KEY = 'SECRET KEY'

class ProductionConfig(Config):
    DEBUG = False

    # Pagination
    POSTS_PER_PAGE = 5

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@host/db'

class DevelopmentConfig(Config):
    DEBUG = True

    # Pagination
    POSTS_PER_PAGE = 2

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../../app.db'

class TestingConfig(Config):
    pass