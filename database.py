import sqlite3
import os
import sys
import shutil
from flask import g

# 获取数据库绝对路径
def get_database_path():
    if getattr(sys, 'frozen', False):
        # 打包后exe运行时，直接使用打包资源中的数据库
        return os.path.join(sys._MEIPASS, 'database.db')
    else:
        # 开发环境
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')

DATABASE = get_database_path()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_app(app):
    app.teardown_appcontext(close_db)
    # 初始化数据库表结构
    with app.app_context():
        db = get_db()
        try:
            # 检查表是否存在
            cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='answer_records'")
            if not cursor.fetchone():
                # 表不存在，创建表
                db.execute("""
                    CREATE TABLE answer_records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        question_id INTEGER NOT NULL,
                        is_correct INTEGER NOT NULL,
                        answer TEXT,
                        create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        is_removed_from_wrong INTEGER DEFAULT 0,
                        is_deleted INTEGER DEFAULT 0
                    )
                """)
                db.commit()
            else:
                # 表存在，检查字段
                cursor = db.execute("PRAGMA table_info(answer_records)")
                columns = [row[1] for row in cursor.fetchall()]
                if 'is_removed_from_wrong' not in columns:
                    db.execute("ALTER TABLE answer_records ADD COLUMN is_removed_from_wrong INTEGER DEFAULT 0")
                    db.commit()
                if 'is_deleted' not in columns:
                    db.execute("ALTER TABLE answer_records ADD COLUMN is_deleted INTEGER DEFAULT 0")
                    db.commit()
        except Exception as e:
            print(f"数据库初始化错误: {e}")
            raise

def close_db(e=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
