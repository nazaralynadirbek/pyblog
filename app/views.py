# -*- coding: utf-8 -*-

from app import app

# Flask modules
from flask import redirect
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return redirect('/articles/')

@app.route('/about')
def about():
    return redirect('/articles/')

@app.route('/articles/')
def articles():
    return render_template('default/content/articles.html')

@app.route('/articles/<article>')
def article(article):
    return render_template('default/content/articles.html')