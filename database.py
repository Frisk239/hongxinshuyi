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
    # 确保answer_records表有is_removed_from_wrong字段
    with app.app_context():
        db = get_db()
        cursor = db.execute("PRAGMA table_info(answer_records)")
        columns = [row[1] for row in cursor.fetchall()]
        if 'is_removed_from_wrong' not in columns:
            db.execute("ALTER TABLE answer_records ADD COLUMN is_removed_from_wrong INTEGER DEFAULT 0")
            db.commit()
        if 'is_deleted' not in columns:
            db.execute("ALTER TABLE answer_records ADD COLUMN is_deleted INTEGER DEFAULT 0")
            db.commit()

def close_db(e=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
