from flask import Flask, render_template, request, jsonify, redirect, url_for, session, g
import sqlite3
import os
from openai import OpenAI
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 生产环境应使用更安全的随机字符串

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
        
        if user is None:
            return '用户不存在', 401
        if user['password'] == password:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['avatar_path'] = user['avatar_path'] or 'static/image/default_touxiang.png'
            return redirect(url_for('index'))
        return '密码错误', 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        avatar = request.files.get('avatar')
        
        db = get_db()
        try:
            avatar_path = f"uploads/{avatar.filename}" if avatar else None
            if avatar:
                os.makedirs('static/uploads', exist_ok=True)
                avatar.save(f'static/{avatar_path}')
                avatar_path = f"uploads/{avatar.filename}"
            
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

@app.route('/user-center')
def user_center():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    db = get_db()
    # 获取用户答题记录
    records = db.execute('''
        SELECT q.question_text, ar.user_answer, ar.is_correct 
        FROM answer_records ar
        JOIN questions q ON ar.question_id = q.id
        WHERE ar.user_id = ?
        ORDER BY ar.id DESC
    ''', (session['user_id'],)).fetchall()
    
    # 获取错题本
    wrong_answers = db.execute('''
        SELECT q.question_text, q.correct_answer, ar.user_answer
        FROM answer_records ar
        JOIN questions q ON ar.question_id = q.id
        WHERE ar.user_id = ? AND ar.is_correct = 0
        ORDER BY ar.id DESC
    ''', (session['user_id'],)).fetchall()
    
    return render_template('user_center.html', records=records, wrong_answers=wrong_answers)

# 题库相关路由
@app.route('/')
def index():
    db = get_db()
    heroes = [
        {
            'id': 1, 
            'name': '毛泽东', 
            'description': '伟大的无产阶级革命家', 
            'image': 'image/image1.png',
            'contributions': [
                '领导中国人民取得新民主主义革命胜利',
                '创立毛泽东思想',
                '建立中华人民共和国'
            ],
            'significance': '毛泽东同志是伟大的马克思主义者，是中国共产党、中国人民解放军和中华人民共和国的主要创立者之一'
        },
        {
            'id': 2,
            'name': '邓小平', 
            'description': '改革开放总设计师', 
            'image': 'image/image2.png',
            'contributions': [
                '提出改革开放政策',
                '提出"一国两制"构想',
                '创立邓小平理论'
            ],
            'significance': '邓小平同志是中国社会主义改革开放和现代化建设的总设计师，邓小平理论的创立者'
        },
        {
            'id': 3,
            'name': '周恩来', 
            'description': '人民的好总理', 
            'image': 'image/image3.png',
            'contributions': [
                '新中国外交事业的主要奠基者',
                '提出和平共处五项原则',
                '为国家建设和发展做出卓越贡献'
            ],
            'significance': '周恩来同志是中国共产党、中华人民共和国和中国人民解放军的主要领导人之一，深受人民爱戴'
        },
        {
            'id': 4,
            'name': '朱德', 
            'description': '红军之父', 
            'image': 'image/image4.png',
            'contributions': [
                '中国人民解放军的主要缔造者之一',
                '参与领导南昌起义',
                '为革命战争胜利做出重大贡献'
            ],
            'significance': '朱德同志是伟大的马克思主义者，无产阶级革命家、政治家和军事家，中国共产党、中国人民解放军和中华人民共和国的主要领导人之一'
        }
    ]
    return render_template('index.html', heroes=heroes)

@app.route('/events/1')
def mao():
    return render_template('events/mao.html')

@app.route('/events/2')
def deng():
    return render_template('events/deng.html')

@app.route('/events/3')
def zhou():
    return render_template('events/zhou.html')

@app.route('/events/4')
def zhu():
    return render_template('events/zhu.html')

@app.route('/questions')
def questions():
    db = get_db()
    questions = db.execute('SELECT * FROM questions').fetchall()
    return render_template('questions.html', questions=questions)

@app.route('/answer')
def answer():
    question_id = request.args.get('question_id')
    random = request.args.get('random', 'false').lower() == 'true'
    db = get_db()
    
    if random:
        question = db.execute('SELECT id, question_text, option_a, option_b, option_c, option_d, correct_answer, difficulty FROM questions ORDER BY RANDOM() LIMIT 1').fetchone()
    else:
        if not question_id:
            return redirect(url_for('answer', random=True))
        question = db.execute('SELECT id, question_text, option_a, option_b, option_c, option_d, correct_answer, difficulty FROM questions WHERE id = ?', (question_id,)).fetchone()
    
    if not question:
        return redirect(url_for('answer', random=True))
    
    return render_template('answer.html', question={
        'id': question['id'],
        'question_text': question['question_text'],
        'option_a': question['option_a'],
        'option_b': question['option_b'],
        'option_c': question['option_c'],
        'option_d': question['option_d'],
        'correct_answer': question['correct_answer'],
        'difficulty': question['difficulty']
    })

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
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        return jsonify({'error': 'DEEPSEEK_API_KEY environment variable not set'}), 500
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    
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
