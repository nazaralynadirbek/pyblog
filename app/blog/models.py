# -*- coding: utf-8 -*-

from app.blog import db

from sqlalchemy_utils import observes

from slugify import slugify
from werkzeug.security import generate_password_hash, check_password_hash

class Base:
    def save(self):
        db.session.add(self)
        db.session.commit()

class User(db.Model, Base):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    articles = db.relationship('Article', backref='pauthor', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self._set_password(password)

    def _set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Category(db.Model, Base):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())

    articles = db.relationship('Article', backref='pcategory', lazy='dynamic')

    def __init__(self, title=""):
        self.title = title

class Article(db.Model, Base):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.Text())
    url = db.Column(db.String(), index=True)

    created_on = db.Column(db.DateTime(), server_default=db.func.now())
    updated_on = db.Column(db.DateTime(), server_default=db.func.now(), onupdate=db.func.now())

    author = db.Column(db.Integer(), db.ForeignKey('user.id'))
    category = db.Column(db.Integer(), db.ForeignKey('category.id'))

    @observes('title')
    def _url(self, title):
        self.url = slugify(title)