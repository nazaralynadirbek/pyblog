# -*- coding: utf-8 -*-

from app import app

# Flask modules
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('default/content/articles.html')