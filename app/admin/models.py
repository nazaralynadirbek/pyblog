# -*- coding: utf-8 -*-

from app.blog.models import Category, Article

from flask_admin.contrib.sqla import ModelView

class CategoryView(ModelView):
    form_excluded_columns = ('articles')

class ArticleView(ModelView):
    form_excluded_columns = ('url', 'created_on', 'updated_on')