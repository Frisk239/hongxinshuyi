import sqlite3
from flask import g

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_app(app):
    app.teardown_appcontext(close_db)

def close_db(e=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
