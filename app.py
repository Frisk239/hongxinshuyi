from flask import Flask, render_template, request, jsonify, redirect, url_for, session, g
import sqlite3
import os
from openai import OpenAI
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 生产环境应使用更安全的随机字符串
import io

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 初始化数据库
from database import get_db, init_app
import os

init_app(app)

# 检查并添加avatar_blob字段
with app.app_context():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'avatar_blob' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN avatar_blob BLOB")
        db.commit()

# 用户认证相关路由
@app.route('/upload-avatar', methods=['POST'])
def upload_avatar():
    # 检查用户是否登录
    if 'user_id' not in session:
        return jsonify({'error': '用户未登录'}), 401
    # 检查是否有文件上传
    if 'avatar' not in request.files:
        return jsonify({'error': '未选择文件'}), 400
    
    file = request.files['avatar']
    if file.filename == '':
        return jsonify({'error': '未选择文件'}), 400
    
    # 验证文件类型
    if not allowed_file(file.filename):
        return jsonify({'error': '不支持的文件类型，仅允许png, jpg, jpeg, gif'}), 400
    
    # 读取文件内容
    avatar_blob = file.read()
    
    # 验证文件大小 (限制2MB)
    if len(avatar_blob) > 2 * 1024 * 1024:
        return jsonify({'error': '文件大小不能超过2MB'}), 400
    
    # 验证文件内容不为空
    if len(avatar_blob) == 0:
        return jsonify({'error': '文件内容为空，请选择有效的图片文件'}), 400
    
    # 保存到数据库
    try:
        db = get_db()
        # 直接覆盖更新头像BLOB数据
        db.execute('UPDATE users SET avatar_blob = ? WHERE id = ?', (avatar_blob, session['user_id']))
        db.commit()
        return jsonify({'success': True})
    except sqlite3.Error as e:
        db.rollback()
        return jsonify({'error': f'数据库错误: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'服务器错误: {str(e)}'}), 500

@app.route('/get-avatar')
def get_avatar():
    if 'user_id' not in session:
        return '', 401
    
    db = get_db()
    user = db.execute('SELECT avatar_blob FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    
    if user and user['avatar_blob']:
        return user['avatar_blob'], 200, {'Content-Type': 'image/jpeg'}
    
    # 返回默认头像
    default_avatar_path = os.path.join(app.root_path, 'static', 'image', 'default_touxiang.png')
    try:
        with open(default_avatar_path, 'rb') as f:
            default_avatar = f.read()
        return default_avatar, 200, {'Content-Type': 'image/png'}
    except FileNotFoundError:
        return jsonify({'error': '默认头像文件不存在'}), 404

@app.route('/get-avatar-by-username/<username>')
def get_avatar_by_username(username):
    db = get_db()
    user = db.execute('SELECT avatar_blob FROM users WHERE username = ?', (username,)).fetchone()
    
    if user and user['avatar_blob']:
        return user['avatar_blob'], 200, {'Content-Type': 'image/png'}
    else:
        try:
            default_avatar_path = os.path.join(app.root_path, 'static', 'image', 'default_touxiang.png')
            with open(default_avatar_path, 'rb') as f:
                default_avatar = f.read()
            return default_avatar, 200, {'Content-Type': 'image/png'}
        except FileNotFoundError:
            return jsonify({'error': '默认头像文件不存在'}), 404

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
            return render_template('login.html', error='用户不存在'), 401
        if user['password'] == password:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('index'))
        return render_template('login.html', error='密码错误'), 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        def calculate_username_length(username):
            length = 0
            for char in username:
                # 中文字符Unicode范围：0x4e00-0x9fff
                if '\u4e00' <= char <= '\u9fff':
                    length += 2
                else:
                    length += 1
            return length

        username = request.form['username']
        if calculate_username_length(username) > 20:
            return '用户名不能超过20个字符（中文字符算2个字符）', 400
        password = request.form['password']
        avatar = request.files.get('avatar')
        avatar_blob = None
        if avatar and avatar.filename:
            # 验证文件类型
            if not allowed_file(avatar.filename):
                return '不支持的文件类型，仅允许png, jpg, jpeg, gif', 400
            # 读取文件内容
            avatar_blob = avatar.read()
            # 验证文件大小
            if len(avatar_blob) > 2 * 1024 * 1024:
                return '文件大小不能超过2MB', 400
        
        db = get_db()
        try:
            db.execute(
                'INSERT INTO users (username, password, avatar_blob) VALUES (?, ?, ?)',
                (username, password, avatar_blob)
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

@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            old_password = data['old_password']
            new_password = data['new_password']
        else:
            old_password = request.form['old_password']
            new_password = request.form['new_password']
            confirm_password = request.form['confirm_password']
            if new_password != confirm_password:
                return jsonify({'error': '两次输入的新密码不一致'}), 400
            
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE id = ?', (session['user_id'],)
        ).fetchone()
        
        if user['password'] != old_password:
            return jsonify({'error': '原密码错误'}), 401
            
        db.execute(
            'UPDATE users SET password = ? WHERE id = ?',
            (new_password, session['user_id'])
        )
        db.commit()
        
        if request.is_json:
            return jsonify({'success': True})
        return redirect(url_for('user_center'))
    
    return render_template('change_password.html')

@app.route('/api/change-password', methods=['POST'])
def api_change_password():
    return change_password()

@app.route('/delete-account', methods=['GET'])
def delete_account_page():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('delete_account.html')

@app.route('/api/delete-account', methods=['POST'])
def delete_account():
    if 'user_id' not in session:
        return jsonify({'error': '未登录'}), 401

    data = request.get_json()
    password = data['password']
    db = get_db()
    user = db.execute(
        'SELECT * FROM users WHERE id = ?', (session['user_id'],)
    ).fetchone()

    if user['password'] != password:
        return jsonify({'error': '密码错误'}), 401

    # 删除用户相关数据
    db.execute('DELETE FROM answer_records WHERE user_id = ?', (session['user_id'],))
    db.execute('DELETE FROM users WHERE id = ?', (session['user_id'],))
    db.commit()

    session.clear()
    return jsonify({'success': True})

@app.route('/user-center')
def user_center():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # 确保session中有avatar_path
    if 'avatar_path' not in session:
        db = get_db()
        user = db.execute('SELECT avatar_path FROM users WHERE id = ?', (session['user_id'],)).fetchone()
        session['avatar_path'] = user['avatar_path'] if user['avatar_path'] else 'image/default_touxiang.png'
    
    # 获取用户答题统计
    db = get_db()
    total_answers = db.execute('SELECT COUNT(*) FROM answer_records WHERE user_id = ?', (session['user_id'],)).fetchone()[0]
    correct_answers = db.execute('SELECT COUNT(*) FROM answer_records WHERE user_id = ? AND is_correct = 1', (session['user_id'],)).fetchone()[0]
    wrong_answers = total_answers - correct_answers
    correct_rate = round((correct_answers / total_answers) * 100) if total_answers > 0 else 0
    
    return render_template('user_center.html', 
                          total_answers=total_answers, 
                          correct_rate=correct_rate, 
                          wrong_answers=wrong_answers)

@app.route('/answer-history')
def answer_history():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    db = get_db()
    records = db.execute('''
        SELECT ar.id, q.question_text, q.option_a, q.option_b, q.option_c, q.option_d, 
               ar.user_answer, q.correct_answer, ar.is_correct
        FROM answer_records ar
        JOIN questions q ON ar.question_id = q.id
        WHERE ar.user_id = ? AND ar.is_deleted = 0
        ORDER BY ar.id DESC
    ''', (session['user_id'],)).fetchall()
    
    return render_template('answer_history.html', records=records)

@app.route('/wrong-questions')
def wrong_questions():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    db = get_db()
    wrong_answers = db.execute('''
        SELECT q.id, q.question_text, q.option_a, q.option_b, q.option_c, q.option_d, 
               q.correct_answer, ar.user_answer
        FROM answer_records ar
        JOIN questions q ON ar.question_id = q.id
        WHERE ar.user_id = ? AND ar.is_correct = 0 AND ar.is_removed_from_wrong = 0
        GROUP BY q.id
        ORDER BY MAX(ar.id) DESC
    ''', (session['user_id'],)).fetchall()
    
    return render_template('wrong_questions.html', wrong_questions=wrong_answers)

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
        },
        {
            'id': 5, 
            'name': '林觉民', 
            'description': '黄花岗七十二烈士之一', 
            'image': 'image/image5.jpg',
            'contributions': [
                '参加黄花岗起义',
                '写下《与妻书》千古绝唱',
                '为革命事业英勇就义'
            ],
            'significance': '林觉民是辛亥革命时期的杰出革命家，以生命诠释了爱国精神'
        },
        {
            'id': 6, 
            'name': '李大钊', 
            'description': '中国共产主义运动的先驱', 
            'image': 'image/image6.jpg',
            'contributions': [
                '传播马克思主义思想',
                '参与创建中国共产党',
                '领导北方革命运动'
            ],
            'significance': '李大钊是中国最早的马克思主义者之一，为中国革命事业奠定了思想基础'
        },
        {
            'id': 7, 
            'name': '董存瑞', 
            'description': '舍身炸碉堡的革命烈士', 
            'image': 'image/image7.jpg',
            'contributions': [
                '在战斗中舍身炸碉堡',
                '为部队开辟前进道路',
                '被追授"战斗英雄"称号'
            ],
            'significance': '董存瑞用生命诠释了革命英雄主义精神，是全国人民学习的榜样'
        },
        {
            'id': 8, 
            'name': '黄继光', 
            'description': '抗美援朝特级英雄', 
            'image': 'image/image8.jpg',
            'contributions': [
                '抗美援朝战争中舍身堵枪眼',
                '为部队冲锋扫清障碍',
                '被追授"特级英雄"称号'
            ],
            'significance': '黄继光是抗美援朝战争中的英雄代表，展现了中华民族的英雄气概'
        },
        {
            'id': 9, 
            'name': '刘胡兰', 
            'description': '生的伟大，死的光荣', 
            'image': 'image/image9.jpg',
            'contributions': [
                '积极参加革命工作',
                '面对敌人坚贞不屈',
                '年仅15岁英勇就义'
            ],
            'significance': '刘胡兰是已知的中国共产党女烈士中年龄最小的之一，毛主席为其题词"生的伟大，死的光荣"'
        },
        {
            'id': 10, 
            'name': '雷锋', 
            'description': '全心全意为人民服务的榜样', 
            'image': 'image/image10.jpg',
            'contributions': [
                '全心全意为人民服务',
                '乐于助人无私奉献',
                '树立了共产主义道德典范'
            ],
            'significance': '雷锋精神影响了几代中国人，成为全心全意为人民服务的象征'
        },
        {
            'id': 11, 
            'name': '焦裕禄', 
            'description': '县委书记的榜样', 
            'image': 'image/image11.jpg',
            'contributions': [
                '带领兰考人民治理风沙',
                '身患重病仍坚持工作',
                '树立了优秀干部的榜样'
            ],
            'significance': '焦裕禄是人民的好干部，"焦裕禄精神"成为党的宝贵财富'
        },
        {
            'id': 12, 
            'name': '王进喜', 
            'description': '铁人精神的代表', 
            'image': 'image/image12.jpg',
            'contributions': [
                '带领工人开发大庆油田',
                '创造"铁人精神"',
                '为中国石油工业发展做出贡献'
            ],
            'significance': '王进喜是新中国石油工业的杰出代表，展现了工人阶级的英雄气概'
        },
        {
            'id': 13, 
            'name': '赵一曼', 
            'description': '抗日民族英雄', 
            'image': 'image/image13.jpg',
            'contributions': [
                '领导东北抗日联军',
                '在战斗中英勇负伤被俘',
                '面对酷刑坚贞不屈'
            ],
            'significance': '赵一曼是中华民族抗日救国的杰出代表，展现了女性革命者的坚强意志'
        },
        {
            'id': 14, 
            'name': '杨靖宇', 
            'description': '东北抗日联军的主要创建者', 
            'image': 'image/image14.jpg',
            'contributions': [
                '创建东北抗日联军',
                '领导艰苦卓绝的抗日游击战争',
                '在绝境中坚持战斗直至牺牲'
            ],
            'significance': '杨靖宇是东北抗日联军的杰出领导人，为国家独立和民族解放事业献出了宝贵生命'
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

@app.route('/events/5')
def lin_jiaomin():
    return render_template('events/lin_jiaomin.html')

@app.route('/events/6')
def li_dazhao():
    return render_template('events/li_dazhao.html')

@app.route('/events/7')
def dong_cunrui():
    return render_template('events/dong_cunrui.html')

@app.route('/events/8')
def huang_jiguang():
    return render_template('events/huang_jiguang.html')

@app.route('/events/9')
def liu_hulan():
    return render_template('events/liu_hulan.html')

@app.route('/events/10')
def lei_feng():
    return render_template('events/lei_feng.html')

@app.route('/events/11')
def jiao_yulu():
    return render_template('events/jiao_yulu.html')

@app.route('/events/12')
def wang_jinxi():
    return render_template('events/wang_jinxi.html')

@app.route('/events/13')
def zhao_yiman():
    return render_template('events/zhao_yiman.html')

@app.route('/events/14')
def yang_jingyu():
    return render_template('events/yang_jingyu.html')

@app.route('/questions')
def questions():
    db = get_db()
    difficulty = request.args.get('difficulty', 'all')
    
    sql = 'SELECT * FROM questions'
    params = []
    
    if difficulty != 'all':
        sql += ' WHERE difficulty = ?'
        params.append(difficulty)
    
    questions = db.execute(sql, params).fetchall()
    return render_template('questions.html', questions=questions, current_difficulty=difficulty)

@app.route('/search')
def search_questions():
    query = request.args.get('q', '')
    difficulty = request.args.get('difficulty', 'all')
    db = get_db()
    
    params = [f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%']
    sql = '''
        SELECT * FROM questions 
        WHERE (question_text LIKE ? 
        OR option_a LIKE ? 
        OR option_b LIKE ? 
        OR option_c LIKE ? 
        OR option_d LIKE ?)
    '''
    
    if difficulty != 'all':
        sql += ' AND difficulty = ?'
        params.append(difficulty)
    
    questions = db.execute(sql, params).fetchall()
    return render_template('questions.html', questions=questions, search_query=query, current_difficulty=difficulty)

@app.route('/answer')
def answer():
    if 'user_id' not in session:
        return redirect(url_for('login'))
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

@app.route('/ranking')
def ranking():
    db = get_db()
    # 获取完整排行榜数据（不限制数量）
    all_ranking_data = db.execute('''
        SELECT u.id as user_id, u.username, 
               COUNT(ar.id) as total_answers, 
               SUM(CASE WHEN ar.is_correct = 1 THEN 1 ELSE 0 END) as correct_count, 
               (SUM(CASE WHEN ar.is_correct = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(ar.id)) as correct_rate
        FROM users u
        LEFT JOIN answer_records ar ON u.id = ar.user_id
        GROUP BY u.id, u.username
        HAVING total_answers > 0
        ORDER BY correct_count DESC, correct_rate DESC
    ''').fetchall()
    
    # 截取前10名用于排行榜显示
    ranking_data = all_ranking_data[:10]
    # 转换元组为字典并计算正确率
    ranking_list = []
    for row in ranking_data:
            user_id, username, total_answers, correct_count, correct_rate = row
            ranking_list.append({
                'user_id': user_id,
                'username': username,
                'total_answers': total_answers,
                'correct_count': correct_count,
                'correct_rate': correct_rate
            })
    
    # 获取当前用户答题数据
    user_id = session.get('user_id')
    user_data = None
    user_rank = None
    
    if user_id:
        # 查询当前用户的答题统计
        user_data = db.execute('''
            SELECT COUNT(ar.id) as total_answers,
                   SUM(CASE WHEN ar.is_correct = 1 THEN 1 ELSE 0 END) as correct_count
            FROM answer_records ar
            WHERE ar.user_id = ?
        ''', (user_id,)).fetchone()
        
        # 从完整排行榜数据中查找用户排名
        user_rank = None
        for index, row in enumerate(all_ranking_data):
            if row['user_id'] == user_id:
                user_rank = index + 1  # 排名从1开始
                break
        
        # 如果用户未上榜（没有答题记录）
        if user_rank is None:
            user_rank = '未上榜'
    
    return render_template('ranking.html', ranking_data=ranking_list, user_data=user_data, user_rank=user_rank)

# API接口
@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    if 'user_id' not in session:
        return jsonify({'error': '未登录'}), 401
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
def api_chat():
    if 'user_id' not in session:
        return jsonify({'error': '未登录，无法使用AI问答功能'}), 401

    data = request.get_json()
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': '问题不能为空'}), 400

    try:
        # 初始化 DeepSeek 客户端
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            print("错误: 未找到DEEPSEEK_API_KEY环境变量")
            return jsonify({'error': '未配置DEEPSEEK_API_KEY环境变量'}), 500
            
        print(f"使用API Key: {api_key[:4]}...{api_key[-4:]}")
        
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
        )

        print(f"发送请求到DeepSeek API，问题: {question}")
        
        # 调用API
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是一个红色文化知识问答助手"},
                {"role": "user", "content": question}
            ],
            "temperature": 0.7,
            "max_tokens": 2000
        }
        print(f"请求参数: {payload}")
        
        try:
            response = client.chat.completions.create(**payload)
            print(f"原始响应: {response}")
        except Exception as e:
            print(f"API调用异常: {str(e)}")
            raise
        
        if not response.choices:
            raise ValueError("API返回空响应")
        
        print(f"收到API响应: {response}")
        
        answer = response.choices[0].message.content
        return jsonify({'answer': answer})

    except Exception as e:
        error_msg = f"API调用失败: {str(e)}"
        print(error_msg)
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': '抱歉，无法获取回答',
            'details': error_msg,
            'solution': '请检查API Key是否正确或联系管理员'
        }), 500

@app.route('/api/check-login')
def check_login():
    return jsonify({
        'logged_in': 'user_id' in session
    })

@app.route('/api/delete-record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    if 'user_id' not in session:
        return jsonify({'error': '未登录'}), 401
    
    db = get_db()
    db.execute('UPDATE answer_records SET is_deleted = 1 WHERE id = ? AND user_id = ?', 
              (record_id, session['user_id']))
    db.commit()
    return jsonify({'success': True})

@app.route('/api/remove-wrong-question/<int:question_id>', methods=['DELETE'])
def remove_wrong_question(question_id):
    if 'user_id' not in session:
        return jsonify({'error': '未登录'}), 401
    
    db = get_db()
    db.execute('''
        UPDATE answer_records 
        SET is_removed_from_wrong = 1
        WHERE question_id = ? AND user_id = ? AND is_correct = 0
    ''', (question_id, session['user_id']))
    db.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
