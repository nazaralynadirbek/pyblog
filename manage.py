# -*- coding: utf-8 -*-

from app.blog import db
from app.blog import app

from app.blog.models import User, Category, Article
from app.admin.models import CategoryView, ArticleView

from flask_admin import Admin
from flask_script import Manager


# Manager
manager = Manager(app)

# Admin
admin = Admin(app, name='microblog', template_mode='bootstrap3')

admin.add_view(CategoryView(Category, db.session))
admin.add_view(ArticleView(Article, db.session))

@manager.command
def migrate():
    """
    Create database and tables

    """

    db.create_all()

# Start point
if __name__ == '__main__':
    manager.run()