# -*- coding: utf-8 -*-

import datetime

from app import app

from app.models import Article, Category

from flask import redirect
from flask import current_app
from flask import render_template

from sqlalchemy import desc

@app.route('/')
@app.route('/index')
def index():
    return redirect('/articles/')

@app.route('/about')
def about():
    return redirect('/')

@app.route('/articles/')
@app.route('/articles/<int:page>')
def articles(page=1):
    articles = Article.query.order_by(desc(Article.id)).\
                             paginate(page, current_app.config['POSTS_PER_PAGE'], True)

    # Arguments
    args = dict()

    return render_template('default/content/articles.html', data=articles, args=args)

@app.route('/articles/<article>')
def article(article):
    article = Article.query.filter_by(url=article).first()

    return render_template('default/content/article.html', data=article)

@app.route('/archive/<int:year>/')
@app.route('/archive/<int:year>/<int:page>')
def archive(year, page=1):
    start = datetime.datetime(year, 1, 1)
    end = datetime.datetime(year, 12, 31)

    articles = Article.query.filter(Article.updated_on >= start,
                                    Article.updated_on <= end).\
                             paginate(page, current_app.config['POSTS_PER_PAGE'], True)

    # Arguments
    args = dict(year=year)

    return render_template('default/content/articles.html', data=articles, args=args)

@app.route('/tag/<category>')
@app.route('/tag/<category>/<int:page>')
def tag(category, page=1):
    articles = Article.query.filter_by(category=Category.query.filter(Category.title.ilike(category)).first().id)\
                            .paginate(page, current_app.config['POSTS_PER_PAGE'], True)

    # Arguments
    args = dict(category=category)

    return render_template('default/content/articles.html', data=articles, args=args)

# Replace it somewhere
@app.context_processor
def archive_processor():
    articles = Article.query.all()

    archive = []
    for article in articles:
        if article.updated_on.year not in archive:
            archive.append(article.updated_on.year)

    return dict(archive=archive)