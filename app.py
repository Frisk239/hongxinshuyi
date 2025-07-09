from flask import Flask, render_template, request, jsonify, redirect, url_for, session, g
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or 'dev-secret-key'

# 初始化数据库
from database import get_db, init_app
init_app(app)

# 用户认证相关路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        return 'Invalid username or password', 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        avatar = request.files.get('avatar')
        
        db = get_db()
        try:
            avatar_path = f"static/uploads/{avatar.filename}" if avatar else None
            if avatar:
                avatar.save(avatar_path)
            
            db.execute(
                'INSERT INTO users (username, password, avatar_path) VALUES (?, ?, ?)',
                (username, password, avatar_path)
            )
            db.commit()
            return redirect(url_for('login'))
        except db.IntegrityError:
            return 'Username already exists', 400
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# 题库相关路由
@app.route('/')
def index():
    db = get_db()
    # 示例英雄数据 - 实际应从数据库获取
    heroes = [
        {'id': 1, 'name': '毛泽东', 'description': '伟大的无产阶级革命家', 'image': 'image/image1.png'},
        {'id': 2, 'name': '邓小平', 'description': '改革开放总设计师', 'image': 'image/image2.png'},
        {'id': 3, 'name': '周恩来', 'description': '人民的好总理', 'image': 'image/image3.png'},
        {'id': 4, 'name': '朱德', 'description': '红军之父', 'image': 'image/image4.png'}
    ]
    return render_template('index.html', heroes=heroes)

@app.route('/questions')
def questions():
    db = get_db()
    questions = db.execute('SELECT * FROM questions').fetchall()
    return render_template('questions.html', questions=questions)

@app.route('/answer')
def answer():
    question_id = request.args.get('question_id')
    random = request.args.get('random')
    db = get_db()
    
    if random:
        question = db.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 1').fetchone()
    else:
        question = db.execute('SELECT * FROM questions WHERE id = ?', (question_id,)).fetchone()
    
    return render_template('answer.html', question=question)

# API接口
@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    db = get_db()
    
    question = db.execute(
        'SELECT * FROM questions WHERE id = ?', (data['question_id'],)
    ).fetchone()
    
    is_correct = data['user_answer'] == question['correct_answer']
    
    if 'user_id' in session:
        db.execute(
            'INSERT INTO answer_records (user_id, question_id, user_answer, is_correct) VALUES (?, ?, ?, ?)',
            (session['user_id'], data['question_id'], data['user_answer'], is_correct)
        )
        db.commit()
    
    return jsonify({
        'correct': is_correct,
        'correct_answer': question['correct_answer']
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    client = OpenAI(api_key=os.getenv('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个党史知识问答助手"},
            {"role": "user", "content": data['message']}
        ],
        stream=False
    )
    
    return jsonify({
        'response': response.choices[0].message.content
    })

@app.route('/api/check-login')
def check_login():
    return jsonify({
        'logged_in': 'user_id' in session
    })

if __name__ == '__main__':
    app.run(debug=True)
