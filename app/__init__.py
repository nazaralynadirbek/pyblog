# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# App
app = Flask(__name__)
app.config.from_object('app.configs.DevelopmentConfig')

# Database
db = SQLAlchemy(app)

# Modules
from app import views