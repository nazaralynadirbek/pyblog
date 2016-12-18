# -*- coding: utf-8 -*-

from app import db
from app import app
from app import models

from flask_script import Manager

# Manager
manager = Manager(app)

@manager.command
def migrate():
    """
    Create database and tables

    """

    db.create_all()

# Start point
if __name__ == '__main__':
    manager.run()