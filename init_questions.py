from database import get_db
from app import app
import sqlite3

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        
        # 创建用户表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            avatar_path TEXT DEFAULT 'static/image/default_touxiang.png',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # 创建问题表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            difficulty INTEGER NOT NULL,
            category TEXT
        )
        ''')
        
        # 创建答题记录表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS answer_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            user_answer TEXT NOT NULL,
            is_correct BOOLEAN NOT NULL,
            answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (question_id) REFERENCES questions (id)
        )
        ''')
        
        db.commit()

def init_questions():
    init_db()  # 先初始化数据库表结构
    with app.app_context():
        db = get_db()
        
        questions = [
            {
                "question_text": "中国共产党成立于哪一年？",
                "option_a": "1919年",
                "option_b": "1921年",
                "option_c": "1949年",
                "option_d": "1978年",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的最高理想和最终目标是什么？",
                "option_a": "实现社会主义现代化",
                "option_b": "实现中华民族伟大复兴",
                "option_c": "实现共产主义",
                "option_d": "实现共同富裕",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党第一次全国代表大会在哪里召开？",
                "option_a": "北京",
                "option_b": "上海",
                "option_c": "广州",
                "option_d": "延安",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "毛泽东思想被确立为党的指导思想是在哪次会议上？",
                "option_a": "中共一大",
                "option_b": "中共七大",
                "option_c": "中共八大",
                "option_d": "中共十一届三中全会",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "改革开放政策是在哪一年提出的？",
                "option_a": "1976年",
                "option_b": "1978年",
                "option_c": "1984年",
                "option_d": "1992年",
                "correct_answer": "B",
                "difficulty": 2
            },
            # 添加更多题目...
            {
                "question_text": "中国特色社会主义最本质的特征是什么？",
                "option_a": "人民民主专政",
                "option_b": "中国共产党领导",
                "option_c": "社会主义市场经济",
                "option_d": "改革开放",
                "correct_answer": "B",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党在社会主义初级阶段的基本路线是什么？",
                "option_a": "以经济建设为中心",
                "option_b": "以政治建设为中心",
                "option_c": "以文化建设为中心",
                "option_d": "以社会建设为中心",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党的根本宗旨是什么？",
                "option_a": "实现共产主义",
                "option_b": "全心全意为人民服务",
                "option_c": "发展生产力",
                "option_d": "维护社会稳定",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "党的十九大报告指出，我国社会主要矛盾已经转化为什么？",
                "option_a": "人民日益增长的物质文化需要同落后的社会生产之间的矛盾",
                "option_b": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾",
                "option_c": "生产力与生产关系之间的矛盾",
                "option_d": "经济基础与上层建筑之间的矛盾",
                "correct_answer": "B",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党领导的多党合作和政治协商制度的基本方针是什么？",
                "option_a": "长期共存、互相监督、肝胆相照、荣辱与共",
                "option_b": "民主协商、共同执政",
                "option_c": "轮流执政、相互制衡",
                "option_d": "一党领导、多党参政",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党的三大作风是什么？",
                "option_a": "理论联系实际、密切联系群众、批评与自我批评",
                "option_b": "实事求是、群众路线、独立自主",
                "option_c": "艰苦奋斗、自力更生、勤俭节约",
                "option_d": "解放思想、与时俱进、求真务实",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党在民主革命时期的三大法宝是什么？",
                "option_a": "统一战线、武装斗争、党的建设",
                "option_b": "土地革命、武装斗争、根据地建设",
                "option_c": "实事求是、群众路线、独立自主",
                "option_d": "理论联系实际、密切联系群众、批评与自我批评",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党人的初心和使命是什么？",
                "option_a": "为中国人民谋幸福，为中华民族谋复兴",
                "option_b": "实现社会主义现代化",
                "option_c": "建设中国特色社会主义",
                "option_d": "推动构建人类命运共同体",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国特色社会主义事业总体布局是什么？",
                "option_a": "四位一体",
                "option_b": "五位一体",
                "option_c": "六位一体",
                "option_d": "七位一体",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "中国特色社会主义制度的最大优势是什么？",
                "option_a": "中国共产党领导",
                "option_b": "人民当家作主",
                "option_c": "社会主义市场经济",
                "option_d": "改革开放",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党在新时代的强军目标是什么？",
                "option_a": "建设一支听党指挥、能打胜仗、作风优良的人民军队",
                "option_b": "实现国防和军队现代化",
                "option_c": "建设世界一流军队",
                "option_d": "维护国家主权和领土完整",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党成立于哪一天？",
                "option_a": "7月1日",
                "option_b": "7月23日",
                "option_c": "8月1日",
                "option_d": "10月1日",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党第一次全国代表大会有多少名代表出席？",
                "option_a": "10名",
                "option_b": "12名",
                "option_c": "15名",
                "option_d": "20名",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党领导中国人民进行的三大革命是什么？",
                "option_a": "新民主主义革命、社会主义革命、改革开放新的伟大革命",
                "option_b": "土地革命、抗日战争、解放战争",
                "option_c": "辛亥革命、新民主主义革命、社会主义革命",
                "option_d": "工业革命、科技革命、文化革命",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党在社会主义初级阶段的基本经济制度是什么？",
                "option_a": "公有制为主体、多种所有制经济共同发展",
                "option_b": "计划经济为主、市场调节为辅",
                "option_c": "社会主义市场经济体制",
                "option_d": "按劳分配为主体、多种分配方式并存",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党在新时代坚持和发展中国特色社会主义的基本方略有多少条？",
                "option_a": "8条",
                "option_b": "10条",
                "option_c": "14条",
                "option_d": "16条",
                "correct_answer": "C",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党领导中国人民取得抗日战争胜利是在哪一年？",
                "option_a": "1945年",
                "option_b": "1949年",
                "option_c": "1950年",
                "option_d": "1953年",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党确立毛泽东思想为党的指导思想是在哪一年？",
                "option_a": "1935年",
                "option_b": "1945年",
                "option_c": "1949年",
                "option_d": "1956年",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党提出'一国两制'构想是为了解决什么问题？",
                "option_a": "台湾问题",
                "option_b": "香港问题",
                "option_c": "澳门问题",
                "option_d": "香港、澳门和台湾问题",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党在社会主义初级阶段的基本路线中的'两个基本点'是什么？",
                "option_a": "改革开放和四项基本原则",
                "option_b": "经济建设和政治建设",
                "option_c": "物质文明建设和精神文明建设",
                "option_d": "国内发展和对外开放",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党领导中国人民进行改革开放的标志性事件是什么？",
                "option_a": "中共十一届三中全会",
                "option_b": "中共十二大",
                "option_c": "南方谈话",
                "option_d": "中共十四大",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党提出的'四个全面'战略布局是什么？",
                "option_a": "全面建设社会主义现代化国家、全面深化改革、全面依法治国、全面从严治党",
                "option_b": "全面建成小康社会、全面深化改革、全面依法治国、全面从严治党",
                "option_c": "经济建设、政治建设、文化建设、社会建设",
                "option_d": "创新、协调、绿色、开放、共享",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党提出的'五位一体'总体布局是什么？",
                "option_a": "经济建设、政治建设、文化建设、社会建设、生态文明建设",
                "option_b": "经济建设、政治建设、文化建设、国防建设、外交建设",
                "option_c": "物质文明建设、精神文明建设、政治文明建设、社会文明建设、生态文明建设",
                "option_d": "创新发展、协调发展、绿色发展、开放发展、共享发展",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党提出的新发展理念是什么？",
                "option_a": "创新、协调、绿色、开放、共享",
                "option_b": "改革、发展、稳定",
                "option_c": "富强、民主、文明、和谐",
                "option_d": "自由、平等、公正、法治",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党提出的社会主义核心价值观在国家层面的价值目标是什么？",
                "option_a": "富强、民主、文明、和谐",
                "option_b": "自由、平等、公正、法治",
                "option_c": "爱国、敬业、诚信、友善",
                "option_d": "和平、发展、合作、共赢",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党提出的'两个一百年'奋斗目标是什么？",
                "option_a": "建党100年时全面建成小康社会，建国100年时建成社会主义现代化国家",
                "option_b": "建党100年时实现现代化，建国100年时实现共产主义",
                "option_c": "建党100年时实现工业化，建国100年时实现现代化",
                "option_d": "建党100年时解决温饱问题，建国100年时达到中等发达国家水平",
                "correct_answer": "A",
                "difficulty": 2
            }
        ]

        # 清空现有题目
        db.execute('DELETE FROM questions')
        db.commit()

        # 插入新题目
        for q in questions:
            db.execute(
                'INSERT INTO questions (question_text, option_a, option_b, option_c, option_d, correct_answer, difficulty) '
                'VALUES (?, ?, ?, ?, ?, ?, ?)',
                (q['question_text'], q['option_a'], q['option_b'], q['option_c'], 
                 q['option_d'], q['correct_answer'], q['difficulty'])
            )
        
        db.commit()
        print(f"成功初始化{len(questions)}道题目")

if __name__ == '__main__':
    init_questions()
