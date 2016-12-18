# -*- coding: utf-8 -*-

from app import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    articles = db.relationship('Article', backref='pauthor', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())

    articles = db.relationship('Article', backref='pcategory', lazy='dynamic')

    def __init__(self, title):
        self.title = title

class Article(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())

    author = db.Column(db.Integer(), db.ForeignKey('user.id'))
    category = db.Column(db.Integer(), db.ForeignKey('category.id'))

    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category