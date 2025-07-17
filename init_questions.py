from database import get_db
from app import app
import sqlite3


def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        # 创建用户表
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           username
                           TEXT
                           UNIQUE
                           NOT
                           NULL,
                           password
                           TEXT
                           NOT
                           NULL,
                           avatar_path
                           TEXT
                           DEFAULT
                           'static/image/default_touxiang.png',
                           created_at
                           TIMESTAMP
                           DEFAULT
                           CURRENT_TIMESTAMP
                       )
                       ''')

        # 创建问题表
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS questions
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           question_text
                           TEXT
                           NOT
                           NULL,
                           option_a
                           TEXT
                           NOT
                           NULL,
                           option_b
                           TEXT
                           NOT
                           NULL,
                           option_c
                           TEXT
                           NOT
                           NULL,
                           option_d
                           TEXT
                           NOT
                           NULL,
                           correct_answer
                           TEXT
                           NOT
                           NULL,
                           difficulty
                           INTEGER
                           NOT
                           NULL,
                           category
                           TEXT
                       )
                       ''')

        # 创建答题记录表
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS answer_records
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           user_id
                           INTEGER
                           NOT
                           NULL,
                           question_id
                           INTEGER
                           NOT
                           NULL,
                           user_answer
                           TEXT
                           NOT
                           NULL,
                           is_correct
                           BOOLEAN
                           NOT
                           NULL,
                           answered_at
                           TIMESTAMP
                           DEFAULT
                           CURRENT_TIMESTAMP,
                           FOREIGN
                           KEY
                       (
                           user_id
                       ) REFERENCES users
                       (
                           id
                       ),
                           FOREIGN KEY
                       (
                           question_id
                       ) REFERENCES questions
                       (
                           id
                       )
                           )
                       ''')

        db.commit()


def init_questions():
    init_db()  # 先初始化数据库表结构
    with app.app_context():
        db = get_db()

        questions = [
            # 简单难度题目 (新增20题)
            {
                "question_text": "中国共产党成立于哪一年？",
                "option_a": "1919 年",
                "option_b": "1921 年",
                "option_c": "1949 年",
                "option_d": "1978 年",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "马克思主义中国化的第一次历史性飞跃是什么？",
                "option_a": "毛泽东思想",
                "option_b": "邓小平理论",
                "option_c": "三个代表重要思想",
                "option_d": "习近平新时代中国特色社会主义思想",
                "correct_answer": "A",
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
                "question_text": "中国共产党成立纪念日是哪一天？",
                "option_a": "7 月 1 日",
                "option_b": "7 月 23 日",
                "option_c": "8 月 1 日",
                "option_d": "10 月 1 日",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国人民抗日战争胜利是在哪一年？",
                "option_a": "1945 年",
                "option_b": "1949 年",
                "option_c": "1950 年",
                "option_d": "1953 年",
                "correct_answer": "A",
                "difficulty": 1
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
                "question_text": "中国共产党的根本宗旨是什么？",
                "option_a": "实现共产主义",
                "option_b": "全心全意为人民服务",
                "option_c": "发展生产力",
                "option_d": "维护社会稳定",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "社会主义核心价值观在国家层面的价值目标是什么？",
                "option_a": "富强、民主、文明、和谐",
                "option_b": "自由、平等、公正、法治",
                "option_c": "爱国、敬业、诚信、友善",
                "option_d": "和平、发展、合作、共赢",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国特色社会主义最本质的特征是什么？",
                "option_a": "人民民主专政",
                "option_b": "中国共产党领导",
                "option_c": "社会主义市场经济",
                "option_d": "改革开放",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "邓小平理论被确立为党的指导思想是在哪次会议上？",
                "option_a": "中共十三大",
                "option_b": "中共十四大",
                "option_c": "中共十五大",
                "option_d": "中共十六大",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "“三个代表” 重要思想的提出者是谁？",
                "option_a": "毛泽东",
                "option_b": "邓小平",
                "option_c": "江泽民",
                "option_d": "胡锦涛",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "科学发展观的核心是什么？",
                "option_a": "发展",
                "option_b": "以人为本",
                "option_c": "全面协调可持续",
                "option_d": "统筹兼顾",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "习近平新时代中国特色社会主义思想是在哪次会议被确立为党的指导思想？",
                "option_a": "中共十七大",
                "option_b": "中共十八大",
                "option_c": "中共十九大",
                "option_d": "中共二十大",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "党的基本路线中的 “一个中心” 指的是什么？",
                "option_a": "以经济建设为中心",
                "option_b": "以政治建设为中心",
                "option_c": "以文化建设为中心",
                "option_d": "以社会建设为中心",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的组织原则是什么？",
                "option_a": "民主集中制",
                "option_b": "少数服从多数",
                "option_c": "下级服从上级",
                "option_d": "全党服从中央",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "入党年龄要求是年满多少周岁？",
                "option_a": "16 周岁",
                "option_b": "18 周岁",
                "option_c": "20 周岁",
                "option_d": "22 周岁",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的象征和标志是什么？",
                "option_a": "党旗",
                "option_b": "党徽",
                "option_c": "党旗和党徽",
                "option_d": "国旗和国徽",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "“四个意识” 具体指政治意识、大局意识、核心意识、什么意识？",
                "option_a": "看齐意识",
                "option_b": "责任意识",
                "option_c": "服务意识",
                "option_d": "创新意识",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "“四个自信” 包括道路自信、理论自信、制度自信和什么自信？",
                "option_a": "文化自信",
                "option_b": "民族自信",
                "option_c": "历史自信",
                "option_d": "发展自信",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "社会主义初级阶段的基本路线核心内容是什么？",
                "option_a": "一个中心，两个基本点",
                "option_b": "四项基本原则",
                "option_c": "改革开放",
                "option_d": "自力更生，艰苦创业",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "“两个维护” 指的是坚决维护习近平总书记党中央的核心、全党的核心地位，坚决维护什么？",
                "option_a": "党中央权威和集中统一领导",
                "option_b": "党的领导",
                "option_c": "社会主义制度",
                "option_d": "人民当家作主",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党章程规定，党员必须履行的义务有多少条？",
                "option_a": "6 条",
                "option_b": "8 条",
                "option_c": "10 条",
                "option_d": "12 条",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "党的最高领导机关是什么？",
                "option_a": "中央政治局",
                "option_b": "中央委员会",
                "option_c": "全国代表大会和中央委员会",
                "option_d": "中央政治局常务委员会",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "党的群众路线的基本内容是什么？",
                "option_a": "一切为了群众，一切依靠群众，从群众中来，到群众中去",
                "option_b": "全心全意为人民服务",
                "option_c": "以人为本",
                "option_d": "密切联系群众",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的三大优良作风不包括以下哪项？",
                "option_a": "理论联系实际",
                "option_b": "密切联系群众",
                "option_c": "批评与自我批评",
                "option_d": "艰苦奋斗",
                "correct_answer": "D",
                "difficulty": 1
            },
            {
                "question_text": "十九大召开的时间是哪一年？",
                "option_a": "2015 年",
                "option_b": "2017 年",
                "option_c": "2019 年",
                "option_d": "2021 年",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党成立以来，共召开了多少次全国代表大会？",
                "option_a": "19 次",
                "option_b": "20 次",
                "option_c": "21 次",
                "option_d": "22 次",
                "correct_answer": "D",
                "difficulty": 1
            },
            {
                "question_text": "社会主义初级阶段的基本经济制度是什么？",
                "option_a": "公有制为主体，多种所有制经济共同发展",
                "option_b": "私有制为主体，多种所有制经济共同发展",
                "option_c": "公有制为主体，私有制为补充",
                "option_d": "混合所有制经济",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的纪律处分有哪几种？",
                "option_a": "警告、严重警告、撤销党内职务、留党察看、开除党籍",
                "option_b": "警告、记过、记大过、降级、撤职",
                "option_c": "警告、严重警告、降级、撤职、开除",
                "option_d": "警告、记过、撤销党内职务、留党察看、开除党籍",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "全面建设社会主义现代化国家的新征程分几个阶段？",
                "option_a": "一个阶段",
                "option_b": "两个阶段",
                "option_c": "三个阶段",
                "option_d": "四个阶段",
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
                "option_a": "1976 年",
                "option_b": "1978 年",
                "option_c": "1984 年",
                "option_d": "1992 年",
                "correct_answer": "B",
                "difficulty": 2
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
                "question_text": "中国共产党确立毛泽东思想为党的指导思想是在哪一年？",
                "option_a": "1935 年",
                "option_b": "1945 年",
                "option_c": "1949 年",
                "option_d": "1956 年",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党提出的 “两个一百年” 奋斗目标是什么？",
                "option_a": "建党 100 年时全面建成小康社会，建国 100 年时建成社会主义现代化国家",
                "option_b": "建党 100 年时实现现代化，建国 100 年时实现共产主义",
                "option_c": "建党 100 年时实现工业化，建国 100 年时实现现代化",
                "option_d": "建党 100 年时解决温饱问题，建国 100 年时达到中等发达国家水平",
                "correct_answer": "A",
                "difficulty": 2
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
                "question_text": "十九大报告指出，我国社会主要矛盾已经转化为什么？",
                "option_a": "人民日益增长的物质文化需要同落后的社会生产之间的矛盾",
                "option_b": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾",
                "option_c": "生产力与生产关系之间的矛盾",
                "option_d": "经济基础与上层建筑之间的矛盾",
                "correct_answer": "B",
                "difficulty": 3
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
                "question_text": "中国共产党领导的人民进行三大革命是什么？",
                "option_a": "新民主主义革命、社会主义革命、改革开放新的伟大革命",
                "option_b": "土地革命、抗日战争、解放战争",
                "option_c": "辛亥革命、新民主主义革命、社会主义革命",
                "option_d": "工业革命、科技革命、文化革命",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党在社会主义初级阶段的基本路线中的 “两个基本点” 是什么？",
                "option_a": "改革开放和四项基本原则",
                "option_b": "经济建设和政治建设",
                "option_c": "物质文明建设和精神文明建设",
                "option_d": "国内发展和对外开放",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党领导的人民进行改革开放的标志性事件是什么？",
                "option_a": "中共十一届三中全会",
                "option_b": "中共十二大",
                "option_c": "南方谈话",
                "option_d": "中共十四大",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党提出的 “四个全面” 战略布局是什么？",
                "option_a": "全面建设社会主义现代化国家、全面深化改革、全面依法治国、全面从严治党",
                "option_b": "全面建成小康社会、全面深化改革、全面依法治国、全面 acee 党",
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
                "option_d": "创新发展、协调发展、acee党、协调发展、共享发展",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党提出的新发展理念是什么？",
                "option_a": "创新、协调、绿色、开放、共享",
                "option_b": "改革、发展、稳定",
                "option_c": "富强、民主、文明、和谐",
                "option_d": "自由、平等、公正、法治",
                "correct_answer": "A",
                "difficulty": 3
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
                "question_text": "中国共产党提出'一国两制'构想是为了解决什么问题？",
                "option_a": "台湾问题",
                "option_b": "香港问题",
                "option_c": "澳门问题",
                "option_d": "香港、澳门和台湾问题",
                "correct_answer": "D",
                "difficulty": 3
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
from database import get_db
from app import app
import sqlite3


def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        # 创建用户表
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           username
                           TEXT
                           UNIQUE
                           NOT
                           NULL,
                           password
                           TEXT
                           NOT
                           NULL,
                           avatar_path
                           TEXT
                           DEFAULT
                           'static/image/default_touxiang.png',
                           created_at
                           TIMESTAMP
                           DEFAULT
                           CURRENT_TIMESTAMP
                       )
                       ''')

        # 创建问题表
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS questions
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           question_text
                           TEXT
                           NOT
                           NULL,
                           option_a
                           TEXT
                           NOT
                           NULL,
                           option_b
                           TEXT
                           NOT
                           NULL,
                           option_c
                           TEXT
                           NOT
                           NULL,
                           option_d
                           TEXT
                           NOT
                           NULL,
                           correct_answer
                           TEXT
                           NOT
                           NULL,
                           difficulty
                           INTEGER
                           NOT
                           NULL,
                           category
                           TEXT
                       )
                       ''')

        # 创建答题记录表
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS answer_records
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           user_id
                           INTEGER
                           NOT
                           NULL,
                           question_id
                           INTEGER
                           NOT
                           NULL,
                           user_answer
                           TEXT
                           NOT
                           NULL,
                           is_correct
                           BOOLEAN
                           NOT
                           NULL,
                           answered_at
                           TIMESTAMP
                           DEFAULT
                           CURRENT_TIMESTAMP,
                           FOREIGN
                           KEY
                       (
                           user_id
                       ) REFERENCES users
                       (
                           id
                       ),
                           FOREIGN KEY
                       (
                           question_id
                       ) REFERENCES questions
                       (
                           id
                       )
                           )
                       ''')

        db.commit()


def init_questions():
    init_db()  # 先初始化数据库表结构
    with app.app_context():
        db = get_db()

        questions = [
            # 简单难度题目 (新增20题)
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
                "question_text": "马克思主义中国化的第一次历史性飞跃是什么？",
                "option_a": "毛泽东思想",
                "option_b": "邓小平理论",
                "option_c": "三个代表重要思想",
                "option_d": "习近平新时代中国特色社会主义思想",
                "correct_answer": "A",
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
                "question_text": "中国共产党成立纪念日是哪一天？",
                "option_a": "7月1日",
                "option_b": "7月23日",
                "option_c": "8月1日",
                "option_d": "10月1日",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国人民抗日战争胜利是在哪一年？",
                "option_a": "1945年",
                "option_b": "1949年",
                "option_c": "1950年",
                "option_d": "1953年",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党人的初心和使命是什么？",
                "option_a": "为中国人民谋幸福，为中华民族谋复兴",
                "option_b": "实现社会主义现代化",
                "option_c": "建设中国特色社会主义",
                "option_d": "推动构建人类命运共同体",
                "correct_answer": "D",
                "difficulty": 1
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
                "question_text": "社会主义核心价值观在国家层面的价值目标是什么？",
                "option_a": "富强、民主、文明、和谐",
                "option_b": "自由、平等、公正、法治",
                "option_c": "爱国、敬业、诚信、友善",
                "option_d": "和平、发展、合作、共赢",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国特色社会主义最本质的特征是什么？",
                "option_a": "人民民主专政",
                "option_b": "中国共产党领导",
                "option_c": "社会主义市场经济",
                "option_d": "改革开放",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "邓小平理论被确立为党的指导思想是在哪次会议上？",
                "option_a": "中共十三大",
                "option_b": "中共十四大",
                "option_c": "中共十五大",
                "option_d": "中共十六大",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "\"三个代表\"重要思想的提出者是谁？",
                "option_a": "毛泽东",
                "option_b": "邓小平",
                "option_c": "江泽民",
                "option_d": "胡锦涛",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "科学发展观的核心是什么？",
                "option_a": "发展",
                "option_b": "以人为本",
                "option_c": "全面协调可持续",
                "option_d": "统筹兼顾",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "习近平新时代中国特色社会主义思想是在哪次会议被确立为党的指导思想？",
                "option_a": "中共十七大",
                "option_b": "中共十八大",
                "option_c": "中共十九大",
                "option_d": "中共二十大",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "党的基本路线中的\"一个中心\"指的是什么？",
                "option_a": "以经济建设为中心",
                "option_b": "以政治建设为中心",
                "option_c": "以文化建设为中心",
                "option_d": "以社会建设为中心",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的组织原则是什么？",
                "option_a": "民主集中制",
                "option_b": "少数服从多数",
                "option_c": "下级服从上级",
                "option_d": "全党服从中央",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "入党年龄要求是年满多少周岁？",
                "option_a": "16周岁",
                "option_b": "18周岁",
                "option_c": "20周岁",
                "option_d": "22周岁",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的象征和标志是什么？",
                "option_a": "党旗",
                "option_b": "党徽",
                "option_c": "党旗和党徽",
                "option_d": "国旗和国徽",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "\"四个意识\"具体指政治意识、大局意识、核心意识、什么意识？",
                "option_a": "看齐意识",
                "option_b": "责任意识",
                "option_c": "服务意识",
                "option_d": "创新意识",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "\"四个自信\"包括道路自信、理论自信、制度自信和什么自信？",
                "option_a": "历史自信",
                "option_b": "民族自信",
                "option_c": "文化自信",
                "option_d": "发展自信",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "社会主义初级阶段的基本路线核心内容是什么？",
                "option_a": "一个中心，两个基本点",
                "option_b": "四项基本原则",
                "option_c": "改革开放",
                "option_d": "自力更生，艰苦创业",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "\"两个维护\"指的是坚决维护习近平总书记党中央的核心、全党的核心地位，坚决维护什么？",
                "option_a": "社会主义制度",
                "option_b": "党的领导",
                "option_c": "党中央权威和集中统一领导",
                "option_d": "人民当家作主",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党章程规定，党员必须履行的义务有多少条？",
                "option_a": "6条",
                "option_b": "8条",
                "option_c": "10条",
                "option_d": "12条",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "党的最高领导机关是什么？",
                "option_a": "中央政治局",
                "option_b": "中央委员会",
                "option_c": "全国代表大会和中央委员会",
                "option_d": "中央政治局常务委员会",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "党的群众路线的基本内容是什么？",
                "option_a": "一切为了群众，一切依靠群众，从群众中来，到群众中去",
                "option_b": "全心全意为人民服务",
                "option_c": "以人为本",
                "option_d": "密切联系群众",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的三大优良作风不包括以下哪项？",
                "option_a": "理论联系实际",
                "option_b": "密切联系群众",
                "option_c": "批评与自我批评",
                "option_d": "艰苦奋斗",
                "correct_answer": "D",
                "difficulty": 1
            },
            {
                "question_text": "十九大召开的时间是哪一年？",
                "option_a": "2015年",
                "option_b": "2017年",
                "option_c": "2019年",
                "option_d": "2021年",
                "correct_answer": "B",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党成立以来，共召开了多少次全国代表大会？",
                "option_a": "19次",
                "option_b": "20次",
                "option_c": "21次",
                "option_d": "22次",
                "correct_answer": "D",
                "difficulty": 1
            },
            {
                "question_text": "社会主义初级阶段的基本经济制度是什么？",
                "option_a": "公有制为主体，多种所有制经济共同发展",
                "option_b": "私有制为主体，多种所有制经济共同发展",
                "option_c": "公有制为主体，私有制为补充",
                "option_d": "混合所有制经济",
                "correct_answer": "A",
                "difficulty": 1
            },
            {
                "question_text": "中国共产党的纪律处分有哪几种？",
                "option_a": "警告、严重警告、降级、撤职、开除",
                "option_b": "警告、记过、记大过、降级、撤职",
                "option_c": "警告、严重警告、撤销党内职务、留党察看、开除党籍",
                "option_d": "警告、记过、撤销党内职务、留党察看、开除党籍",
                "correct_answer": "C",
                "difficulty": 1
            },
            {
                "question_text": "全面建设社会主义现代化国家的新征程分几个阶段？",
                "option_a": "一个阶段",
                "option_b": "两个阶段",
                "option_c": "三个阶段",
                "option_d": "四个阶段",
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
                "option_a": "实事求是、群众路线、独立自主",
                "option_b": "理论联系实际、密切联系群众、批评与自我批评",
                "option_c": "艰苦奋斗、自力更生、勤俭节约",
                "option_d": "解放思想、与时俱进、求真务实",
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
                "option_a": "维护国家主权和领土完整",
                "option_b": "实现国防和军队现代化",
                "option_c": "建设世界一流军队",
                "option_d": "建设一支听党指挥、能打胜仗、作风优良的人民军队",
                "correct_answer": "D",
                "difficulty": 2
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
                "question_text": "中国共产党提出的'两个一百年'奋斗目标是什么？",
                "option_a": "建党100年时全面建成小康社会，建国100年时建成社会主义现代化国家",
                "option_b": "建党100年时实现现代化，建国100年时实现共产主义",
                "option_c": "建党100年时实现工业化，建国100年时实现现代化",
                "option_d": "建党100年时解决温饱问题，建国100年时达到中等发达国家水平",
                "correct_answer": "A",
                "difficulty": 2
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
                "question_text": "十九大报告指出，我国社会主要矛盾已经转化为什么？",
                "option_a": "人民日益增长的物质文化需要同落后的社会生产之间的矛盾",
                "option_b": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾",
                "option_c": "生产力与生产关系之间的矛盾",
                "option_d": "经济基础与上层建筑之间的矛盾",
                "correct_answer": "B",
                "difficulty": 3
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
                "question_text": "中国共产党领导的人民进行三大革命是什么？",
                "option_a": "辛亥革命、新民主主义革命、社会主义革命",
                "option_b": "土地革命、抗日战争、解放战争",
                "option_c": "新民主主义革命、社会主义革命、改革开放新的伟大革命",
                "option_d": "工业革命、科技革命、文化革命",
                "correct_answer": "C",
                "difficulty": 3
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
                "question_text": "中国共产党领导的人民进行改革开放的标志性事件是什么？",
                "option_a": "中共十二大",
                "option_b": "中共十一届三中全会",
                "option_c": "南方谈话",
                "option_d": "中共十四大",
                "correct_answer": "B",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党提出的'四个全面'战略布局是什么？",
                "option_a": "创新、协调、绿色、开放、共享",
                "option_b": "全面建成小康社会、全面深化改革、全面依法治国、全面从严治党",
                "option_c": "经济建设、政治建设、文化建设、社会建设",
                "option_d": "全面建设社会主义现代化国家、全面深化改革、全面依法治国、全面从严治党",
                "correct_answer": "D",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党提出的'五位一体'总体布局是什么？",
                "option_a": "经济建设、政治建设、文化建设、社会建设、生态文明建设",
                "option_b": "经济建设、政治建设、文化建设、国防建设、外交建设",
                "option_c": "物质文明建设、精神文明建设、政治文明建设、社会文明建设、生态文明建设",
                "option_d": "创新发展、协调发展、绿色发展、开放发展、共享发展",
                "correct_answer": "A",
                "difficulty": 3
            },
            {
                "question_text": "中国共产党提出的新发展理念是什么？",
                "option_a": "创新、协调、绿色、开放、共享",
                "option_b": "改革、发展、稳定",
                "option_c": "富强、民主、文明、和谐",
                "option_d": "自由、平等、公正、法治",
                "correct_answer": "A",
                "difficulty": 3
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
                "question_text": "中国共产党提出'一国两制'构想是为了解决什么问题？",
                "option_a": "台湾问题",
                "option_b": "香港问题",
                "option_c": "澳门问题",
                "option_d": "香港、澳门和台湾问题",
                "correct_answer": "D",
                "difficulty": 3
            },
            {
            "question_text": "中国共产党历史上的第一个中央纪律检查机构成立于哪一年？",
            "option_a": "1921年",
            "option_b": "1927年",
            "option_c": "1935年",
            "option_d": "1949年",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "毛泽东同志提出'枪杆子里出政权'的著名论断是在哪个会议上？",
            "option_a": "中共一大",
            "option_b": "八七会议",
            "option_c": "遵义会议",
            "option_d": "瓦窑堡会议",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "中国共产党在抗日战争时期的土地政策是？",
            "option_a": "打土豪分田地",
            "option_b": "减租减息",
            "option_c": "耕者有其田",
            "option_d": "家庭联产承包",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "'百花齐放、百家争鸣'方针提出于哪个历史时期？",
            "option_a": "建国初期",
            "option_b": "改革开放初期",
            "option_c": "社会主义现代化建设新时期",
            "option_d": "新时代",
            "correct_answer": "a",
            "difficulty": 1
        },
        {
            "question_text": "中国共产党首次提出'邓小平理论'科学概念是在党的哪次会议？",
            "option_a": "十三大",
            "option_b": "十四大",
            "option_c": "十五大",
            "option_d": "十六大",
            "correct_answer": "c",
            "difficulty": 1
        },
        {
            "question_text": "我国加入世界贸易组织是在哪一年？",
            "option_a": "1997年",
            "option_b": "2001年",
            "option_c": "2008年",
            "option_d": "2012年",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "'三个代表'重要思想的核心是？",
            "option_a": "代表先进生产力的发展要求",
            "option_b": "代表先进文化的前进方向",
            "option_c": "代表最广大人民的根本利益",
            "option_d": "代表社会主义的发展方向",
            "correct_answer": "c",
            "difficulty": 1
        },
        {
            "question_text": "科学发展观首次提出是在党的哪次会议？",
            "option_a": "十五大",
            "option_b": "十六大",
            "option_c": "十七大",
            "option_d": "十八大",
            "correct_answer": "c",
            "difficulty": 1
        },
        {
            "question_text": "中国共产党的第一部党章制定于哪次全国代表大会？",
            "option_a": "一大",
            "option_b": "二大",
            "option_c": "三大",
            "option_d": "四大",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "'一带一路'倡议正式提出是在哪一年？",
            "option_a": "2012年",
            "option_b": "2013年",
            "option_c": "2015年",
            "option_d": "2017年",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "中国共产党历史上被誉为'生死攸关的转折点'的会议是？",
            "option_a": "八七会议",
            "option_b": "遵义会议",
            "option_c": "洛川会议",
            "option_d": "瓦窑堡会议",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "我国全面取消农业税是在哪一年？",
            "option_a": "2004年",
            "option_b": "2005年",
            "option_c": "2006年",
            "option_d": "2007年",
            "correct_answer": "c",
            "difficulty": 1
        },
        {
            "question_text": "'不忘初心、牢记使命'主题教育首次开展于哪一年？",
            "option_a": "2016年",
            "option_b": "2017年",
            "option_c": "2019年",
            "option_d": "2021年",
            "correct_answer": "c",
            "difficulty": 1
        },
        {
            "question_text": "中国共产党在社会主义初级阶段的基本纲领是在哪次会议上提出的？",
            "option_a": "十三大",
            "option_b": "十四大",
            "option_c": "十五大",
            "option_d": "十六大",
            "correct_answer": "c",
            "difficulty": 1
        },
        {
            "question_text": "我国第一个五年计划实施的时间是？",
            "option_a": "1949-1954年",
            "option_b": "1953-1957年",
            "option_c": "1956-1960年",
            "option_d": "1961-1965年",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "'社会主义核心价值体系'首次提出是在党的哪次会议？",
            "option_a": "十六大",
            "option_b": "十七大",
            "option_c": "十八大",
            "option_d": "十九大",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "中国共产党领导的第一次工人运动高潮的起点是？",
            "option_a": "香港海员大罢工",
            "option_b": "安源路矿工人大罢工",
            "option_c": "京汉铁路工人大罢工",
            "option_d": "省港大罢工",
            "correct_answer": "a",
            "difficulty": 1
        },
        {
            "question_text": "'十四五'规划的实施时间是？",
            "option_a": "2020-2024年",
            "option_b": "2021-2025年",
            "option_c": "2022-2026年",
            "option_d": "2023-2027年",
            "correct_answer": "b",
            "difficulty": 1
        },
        {
            "question_text": "中国共产党提出'构建人类命运共同体'理念是在哪次联合国会议？",
            "option_a": "联合国大会",
            "option_b": "联合国安理会",
            "option_c": "联合国人权理事会",
            "option_d": "联合国气候变化大会",
            "correct_answer": "a",
            "difficulty": 1
        },

        {
            "question_text": "党史学习教育动员大会召开于哪一年？",
            "option_a": "2020年",
            "option_b": "2021年",
            "option_c": "2022年",
            "option_d": "2023年",
            "correct_answer": "b",
            "difficulty": 1
        },
    {
        "question_text": "中国共产党在社会主义初级阶段的基本路线的核心内容是什么？",
        "option_a": "一个中心，两个基本点",
        "option_b": "四项基本原则",
        "option_c": "改革开放",
        "option_d": "自力更生，艰苦创业",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党历史上的三大优良作风不包括下列哪一项？",
        "option_a": "理论联系实际",
        "option_b": "密切联系群众",
        "option_c": "批评与自我批评",
        "option_d": "艰苦奋斗",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "‘五四运动’爆发于哪一年？",
        "option_a": "1911年",
        "option_b": "1919年",
        "option_c": "1921年",
        "option_d": "1949年",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党打响武装反抗国民党反动派第一枪的起义是？",
        "option_a": "秋收起义",
        "option_b": "南昌起义",
        "option_c": "广州起义",
        "option_d": "百色起义",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "‘农村包围城市，武装夺取政权’的革命道路是谁提出的？",
        "option_a": "刘少奇",
        "option_b": "周恩来",
        "option_c": "毛泽东",
        "option_d": "邓小平",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党在长征途中召开的具有转折意义的会议是？",
        "option_a": "遵义会议",
        "option_b": "瓦窑堡会议",
        "option_c": "洛川会议",
        "option_d": "古田会议",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "抗日战争时期，中国共产党领导的八路军取得的第一次大捷是？",
        "option_a": "淞沪会战",
        "option_b": "台儿庄战役",
        "option_c": "百团大战",
        "option_d": "平型关大捷",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "‘两个务必’是毛泽东在党的哪次会议上提出的？",
        "option_a": "七大",
        "option_b": "七届二中全会",
        "option_c": "八大",
        "option_d": "十一届三中全会",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中华人民共和国成立的日期是？",
        "option_a": "1945年8月15日",
        "option_b": "1945年9月2日",
        "option_c": "1949年10月1日",
        "option_d": "1949年10月2日",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党过渡时期总路线的主体是？",
        "option_a": "实现工业化",
        "option_b": "对农业的社会主义改造",
        "option_c": "对手工业的社会主义改造",
        "option_d": "对资本主义工商业的社会主义改造",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "‘三大改造’完成于哪一年？",
        "option_a": "1949年",
        "option_b": "1953年",
        "option_c": "1956年",
        "option_d": "1978年",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第八次全国代表大会召开于哪一年？",
        "option_a": "1945年",
        "option_b": "1956年",
        "option_c": "1966年",
        "option_d": "1978年",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "‘文化大革命’结束的标志是？",
        "option_a": "粉碎‘四人帮’",
        "option_b": "十一届三中全会召开",
        "option_c": "邓小平复出",
        "option_d": "真理标准问题大讨论",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第十一届中央委员会第三次全体会议召开于哪一年？",
        "option_a": "1976年",
        "option_b": "1978年",
        "option_c": "1982年",
        "option_d": "1992年",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "改革开放的总设计师是？",
        "option_a": "毛泽东",
        "option_b": "邓小平",
        "option_c": "江泽民",
        "option_d": "胡锦涛",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第十二次全国代表大会提出的奋斗目标是？",
        "option_a": "建设有中国特色的社会主义",
        "option_b": "全面建设小康社会",
        "option_c": "实现社会主义现代化",
        "option_d": "实现中华民族伟大复兴",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "‘一国两制’的构想最初是为解决哪个问题提出的？",
        "option_a": "香港问题",
        "option_b": "澳门问题",
        "option_c": "台湾问题",
        "option_d": "西藏问题",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第十三次全国代表大会系统阐述了？",
        "option_a": "科学发展观",
        "option_b": "社会主义本质理论",
        "option_c": "三个代表重要思想",
        "option_d": "社会主义初级阶段理论",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "香港回归祖国的时间是？",
        "option_a": "1997年7月1日",
        "option_b": "1999年12月20日",
        "option_c": "1997年12月20日",
        "option_d": "1999年7月1日",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "澳门回归祖国的时间是？",
        "option_a": "1997年7月1日",
        "option_b": "1999年12月20日",
        "option_c": "1997年12月20日",
        "option_d": "1999年7月1日",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第十五次全国代表大会把什么确立为党的指导思想？",
        "option_a": "毛泽东思想",
        "option_b": "邓小平理论",
        "option_c": "三个代表重要思想",
        "option_d": "科学发展观",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "‘三个代表’重要思想的核心是？",
        "option_a": "代表中国先进生产力的发展要求",
        "option_b": "代表中国先进文化的前进方向",
        "option_c": "代表中国最广大人民的根本利益",
        "option_d": "代表中国工人阶级的先锋队性质",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第十六次全国代表大会提出的奋斗目标是？",
        "option_a": "全面建设小康社会",
        "option_b": "建设社会主义现代化强国",
        "option_c": "实现中华民族伟大复兴",
        "option_d": "构建社会主义和谐社会",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "科学发展观的第一要义是？",
        "option_a": "以人为本",
        "option_b": "发展",
        "option_c": "全面协调可持续",
        "option_d": "统筹兼顾",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第十七次全国代表大会召开于哪一年？",
        "option_a": "2002年",
        "option_b": "2007年",
        "option_c": "2012年",
        "option_d": "2017年",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第十八次全国代表大会把什么确立为党的指导思想？",
        "option_a": "邓小平理论",
        "option_b": "三个代表重要思想",
        "option_c": "科学发展观",
        "option_d": "习近平新时代中国特色社会主义思想",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "‘中国梦’的本质是？",
        "option_a": "国家富强、民族振兴、人民幸福",
        "option_b": "实现社会主义现代化",
        "option_c": "建设中国特色社会主义",
        "option_d": "推动构建人类命运共同体",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第十九次全国代表大会召开于哪一年？",
        "option_a": "2012年",
        "option_b": "2017年",
        "option_c": "2022年",
        "option_d": "2018年",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "习近平新时代中国特色社会主义思想的核心要义是？",
        "option_a": "坚持和发展中国特色社会主义",
        "option_b": "实现中华民族伟大复兴",
        "option_c": "推动构建人类命运共同体",
        "option_d": "全面从严治党",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "‘两个一百年’奋斗目标中，第一个一百年的目标是？",
        "option_a": "全面建成小康社会",
        "option_b": "全面建设社会主义现代化国家",
        "option_c": "实现中华民族伟大复兴",
        "option_d": "基本实现社会主义现代化",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党第二十次全国代表大会召开于哪一年？",
        "option_a": "2017年",
        "option_b": "2020年",
        "option_c": "2022年",
        "option_d": "2023年",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "党的二十大报告指出，我国社会主要矛盾是什么？",
        "option_a": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾",
        "option_b": "人民日益增长的物质文化需要同落后的社会生产之间的矛盾",
        "option_c": "阶级矛盾",
        "option_d": "贫富差距矛盾",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "‘四个全面’战略布局中，居于引领地位的是？",
        "option_a": "全面深化改革",
        "option_b": "全面建设社会主义现代化国家",
        "option_c": "全面依法治国",
        "option_d": "全面从严治党",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "‘五位一体’总体布局不包括下列哪一项？",
        "option_a": "经济建设",
        "option_b": "政治建设",
        "option_c": "文化建设",
        "option_d": "生态文明建设",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的最高领导机关是？",
        "option_a": "中央委员会",
        "option_b": "中央政治局",
        "option_c": "中央政治局常务委员会",
        "option_d": "党的全国代表大会和中央委员会",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "党的纪律中最重要、最根本、最关键的纪律是？",
        "option_a": "政治纪律",
        "option_b": "组织纪律",
        "option_c": "廉洁纪律",
        "option_d": "群众纪律",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党党员的党龄从何时开始计算？",
        "option_a": "入党申请之日",
        "option_b": "入党积极分子确定之日",
        "option_c": "预备党员转正之日",
        "option_d": "预备党员之日",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的党旗为旗面缀有什么图案的红旗？",
        "option_a": "金黄色党徽图案",
        "option_b": "黄色五角星图案",
        "option_c": "镰刀和锤头组成的图案",
        "option_d": "镰刀和斧头组成的图案",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的党徽图案由什么组成？",
        "option_a": "镰刀和锤头",
        "option_b": "镰刀和斧头",
        "option_c": "锤子和斧头",
        "option_d": "镰刀和五星",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "‘一带一路’倡议是指？",
        "option_a": "21世纪海上丝绸之路和中欧班列",
        "option_b": "丝绸之路经济带和中欧班列",
        "option_c": "丝绸之路经济带和21世纪海上丝绸之路",
        "option_d": "丝绸之路和海上丝绸之路",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党提出的‘人类命运共同体’理念首次被写入联合国文件是在哪一年？",
        "option_a": "2015年",
        "option_b": "2016年",
        "option_c": "2017年",
        "option_d": "2018年",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "‘不忘初心、牢记使命’主题教育的总要求是？",
        "option_a": "守初心、担使命，找差距、抓落实",
        "option_b": "不忘初心、继续前进",
        "option_c": "解放思想、实事求是",
        "option_d": "全心全意为人民服务",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "‘两学一做’学习教育指的是学党章党规、学系列讲话，做什么？",
        "option_a": "合格党员",
        "option_b": "优秀党员",
        "option_c": "模范党员",
        "option_d": "先进党员",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的根本组织原则是？",
        "option_a": "民下级服从上级",
        "option_b": "少数服从多数",
        "option_c": "主集中制",
        "option_d": "全党服从中央",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的最大政治优势是？",
        "option_a": "密切联系群众",
        "option_b": "实事求是",
        "option_c": "独立自主",
        "option_d": "统一战线",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党执政后的最大危险是？",
        "option_a": "腐败",
        "option_b": "脱离群众",
        "option_c": "能力不足",
        "option_d": "精神懈怠",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "党的群众路线的基本内容是？",
        "option_a": "相信群众，依靠群众",
        "option_b": "全心全意为人民服务",
        "option_c": "向人民负责，为人民服务",
        "option_d": "一切为了群众，一切依靠群众，从群众中来，到群众中去",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的三大法宝是？",
        "option_a": "统一战线、武装斗争、党的建设",
        "option_b": "实事求是、群众路线、独立自主",
        "option_c": "理论联系实际、密切联系群众、批评与自我批评",
        "option_d": "政治建设、思想建设、组织建设",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "‘四个伟大’中起决定性作用的是？",
        "option_a": "伟大斗争",
        "option_b": "伟大工程",
        "option_c": "伟大事业",
        "option_d": "伟大梦想",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国特色社会主义进入新时代的标志是？",
        "option_a": "新中国成立",
        "option_b": "党的十九大召开",
        "option_c": "党的十八大召开",
        "option_d": "改革开放",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "新时代我国社会的主要矛盾已经转化为？",
        "option_a": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾",
        "option_b": "人民日益增长的物质文化需要同落后的社会生产之间的矛盾",
        "option_c": "经济基础和上层建筑之间的矛盾",
        "option_d": "生产力和生产关系之间的矛盾",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "习近平总书记提出的‘三严三实’中，‘三严’不包括下列哪一项？",
        "option_a": "严以修身",
        "option_b": "严以用权",
        "option_c": "严以律己",
        "option_d": "严以待人",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "‘两个维护’是指坚决维护习近平总书记党中央的核心、全党的核心地位，坚决维护？",
        "option_a": "社会主义制度",
        "option_b": "党的领导",
        "option_c": "党中央权威和集中统一领导",
        "option_d": "人民当家作主",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党成立的标志是？",
        "option_a": "五四运动爆发",
        "option_b": "中共一大召开",
        "option_c": "马克思主义在中国传播",
        "option_d": "辛亥革命胜利",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的性质是？",
        "option_a": "中国工人阶级的先锋队，同时是中国人民和中华民族的先锋队",
        "option_b": "中国工人阶级的先锋队",
        "option_c": "中国人民和中华民族的先锋队",
        "option_d": "无产阶级政党",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的指导思想不包括下列哪一项？",
        "option_a": "马克思列宁主义",
        "option_b": "毛泽东思想",
        "option_c": "邓小平理论",
        "option_d": "孙中山三民主义",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党章程规定，党的最高理想和最终目标是？",
        "option_a": "实现中华民族伟大复兴",
        "option_b": "实现社会主义现代化",
        "option_c": "实现共产主义",
        "option_d": "全面建成小康社会",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党在社会主义初级阶段的基本路线的完整表述是？",
        "option_a": "领导和团结全国各族人民，以经济建设为中心，坚持四项基本原则，坚持改革开放，自力更生，艰苦创业，为把我国建设成为富强民主文明和谐美丽的社会主义现代化强国而奋斗",
        "option_b": "以经济建设为中心，坚持四项基本原则，坚持改革开放",
        "option_c": "领导和团结全国各族人民，以经济建设为中心，坚持四项基本原则，坚持改革开放",
        "option_d": "自力更生，艰苦创业，为把我国建设成为富强民主文明和谐美丽的社会主义现代化强国而奋斗",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "四项基本原则的核心是？",
        "option_a": "坚持社会主义道路",
        "option_b": "坚持党的领导",
        "option_c": "坚持人民民主专政",
        "option_d": "坚持马克思列宁主义、毛泽东思想",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "改革开放是中国共产党在新的历史条件下领导人民进行的新的伟大革命，是决定当代中国命运的？",
        "option_a": "唯一选择",
        "option_b": "必然选择",
        "option_c": "重要选择",
        "option_d": "关键抉择",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国特色社会主义道路的必由之路是？",
        "option_a": "改革开放",
        "option_b": "独立自主",
        "option_c": "自力更生",
        "option_d": "艰苦奋斗",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国特色社会主义制度的最大优势是？",
        "option_a": "依法治国",
        "option_b": "人民当家作主",
        "option_c": "中国共产党领导",
        "option_d": "改革开放",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的根本宗旨是？",
        "option_a": "实现共产主义",
        "option_b": "全心全意为人民服务",
        "option_c": "发展生产力",
        "option_d": "建设社会主义现代化强国",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的思想路线是？",
        "option_a": "一切从实际出发，理论联系实际，实事求是，在实践中检验真理和发展真理",
        "option_b": "解放思想，实事求是",
        "option_c": "实事求是，群众路线，独立自主",
        "option_d": "与时俱进，开拓创新",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的组织路线的核心是？",
        "option_a": "干部问题",
        "option_b": "组织原则",
        "option_c": "组织制度",
        "option_d": "党员队伍建设",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的纪律处分不包括下列哪一项？",
        "option_a": "警告",
        "option_b": "严重警告",
        "option_c": "记过",
        "option_d": "撤销党内职务",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党党员必须履行的义务不包括下列哪一项？",
        "option_a": "认真学习马克思列宁主义、毛泽东思想、邓小平理论、‘三个代表’重要思想、科学发展观、习近平新时代中国特色社会主义思想",
        "option_b": "贯彻执行党的基本路线和各项方针、政策",
        "option_c": "对党的决议和政策如有不同意见，可以声明保留，并且可以把自己的意见向党的上级组织直至中央提出",
        "option_d": "维护党的团结和统一，对党忠诚老实，言行一致，坚决反对一切派别组织和小集团活动，反对阳奉阴违的两面派行为和一切阴谋诡计",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党党员享有的权利不包括下列哪一项？",
        "option_a": "参加党的有关会议，阅读党的有关文件，接受党的教育和培训",
        "option_b": "在党的会议上和党报党刊上，参加关于党的政策问题的讨论",
        "option_c": "对党的工作提出建议和倡议",
        "option_d": "要求罢免或撤换不称职的干部",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "发展党员，必须把什么放在首位？",
        "option_a": "政治标准",
        "option_b": "业务能力",
        "option_c": "群众公认",
        "option_d": "工作业绩",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "预备党员的预备期为多久？",
        "option_a": "半年",
        "option_b": "一年",
        "option_c": "一年半",
        "option_d": "两年",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "预备党员的权利，除了没有下列哪一项以外，同正式党员一样？",
        "option_a": "参加党的有关会议的权利",
        "option_b": "表决权、选举权和被选举权",
        "option_c": "阅读党的有关文件的权利",
        "option_d": "接受党的教育和培训的权利",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "党的基层组织是党在社会基层组织中的战斗堡垒，是党的？",
        "option_a": "基本单位",
        "option_b": "重要组成部分",
        "option_c": "全部工作和战斗力的基础",
        "option_d": "细胞",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "党的基层委员会每届任期多久？",
        "option_a": "五年至七年",
        "option_b": "两年至三年",
        "option_c": "三年至五年",
        "option_d": "一年至两年",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "党的纪律是党的各级组织和全体党员必须遵守的行为规则，是维护党的团结统一、完成党的任务的？",
        "option_a": "前提",
        "option_b": "基础",
        "option_c": "关键",
        "option_d": "保证",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "对党员的纪律处分，必须经过支部大会讨论决定，报党的哪一级组织批准？",
        "option_a": "市级委员会",
        "option_b": "县级委员会",
        "option_c": "基层委员会",
        "option_d": "省级委员会",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "党组织对违犯党的纪律的党员，应当本着什么精神，按照错误性质和情节轻重，给以批评教育直至纪律处分？",
        "option_a": "惩前毖后、治病救人",
        "option_b": "实事求是",
        "option_c": "严肃认真",
        "option_d": "教育为主、惩罚为辅",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的中央委员会每届任期多久？",
        "option_a": "四年",
        "option_b": "五年",
        "option_c": "三年",
        "option_d": "六年",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "党的全国代表大会每几年举行一次？",
        "option_a": "三年",
        "option_b": "四年",
        "option_c": "五年",
        "option_d": "六年",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党章程由党的哪次会议制定和修改？",
        "option_a": "中央委员会",
        "option_b": "全国代表大会",
        "option_c": "中央政治局",
        "option_d": "中央政治局常务委员会",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的中央军事委员会实行什么负责制？",
        "option_a": "集体负责制",
        "option_b": "主席负责制",
        "option_c": "民主集中制",
        "option_d": "分工负责制",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党同各民主党派合作的基本方针是？",
        "option_a": "长期共存、互相监督、肝胆相照、荣辱与共",
        "option_b": "长期共存、互相监督",
        "option_c": "肝胆相照、荣辱与共",
        "option_d": "长期共存、荣辱与共",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党领导的多党合作和政治协商制度是我国的一项？",
        "option_a": "重要政治制度",
        "option_b": "根本政治制度",
        "option_c": "基本政治制度",
        "option_d": "一般政治制度",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "我国的根本政治制度是？",
        "option_a": "基层群众自治制度",
        "option_b": "中国共产党领导的多党合作和政治协商制度",
        "option_c": "民族区域自治制度",
        "option_d": "人民代表大会制度",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "我国的基本经济制度是？",
        "option_a": "计划经济为主、市场经济为辅",
        "option_b": "私有制为主体、多种所有制经济共同发展",
        "option_c": "公有制为主体、私有制为补充",
        "option_d": "公有制为主体、多种所有制经济共同发展",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "社会主义的本质是？",
        "option_a": "解放生产力，发展生产力，消灭剥削，消除两极分化，最终达到共同富裕",
        "option_b": "公有制为主体，多种所有制经济共同发展",
        "option_c": "人民当家作主",
        "option_d": "依法治国",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "科学技术是第一生产力，是谁提出的？",
        "option_a": "毛泽东",
        "option_b": "邓小平",
        "option_c": "江泽民",
        "option_d": "胡锦涛",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "创新是引领发展的第一动力，是谁提出的？",
        "option_a": "江泽民",
        "option_b": "邓小平",
        "option_c": "习近平",
        "option_d": "胡锦涛",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "我国发展新的历史方位是？",
        "option_a": "实现中华民族伟大复兴",
        "option_b": "全面建设社会主义现代化国家",
        "option_c": "中国特色社会主义进入新时代",
        "option_d": "全面建成小康社会",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "新时代党的建设总要求中，以什么为统领？",
        "option_a": "政治建设",
        "option_b": "思想建设",
        "option_c": "组织建设",
        "option_d": "作风建设",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "全面从严治党，核心是加强党的领导，基础在全面，关键在严，要害在？",
        "option_a": "治",
        "option_b": "管",
        "option_c": "抓",
        "option_d": "防",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "‘四风’问题是指形式主义、官僚主义、享乐主义和？",
        "option_a": "宗派主义",
        "option_b": "拜金主义",
        "option_c": "个人主义",
        "option_d": "奢靡之风",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的历史上，第一个中央纪律检查机构是？",
        "option_a": "中央纪律检查委员会",
        "option_b": "中央监察委员会",
        "option_c": "中央审查委员会",
        "option_d": "中央检察委员会",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党巡视工作的方针是？",
        "option_a": "实事求是、客观公正",
        "option_b": "全面覆盖、突出重点",
        "option_c": "发现问题、形成震慑、推动改革、促进发展",
        "option_d": "依规依纪、安全保密",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党廉洁自律准则对党员和党员领导干部提出了几条规范？",
        "option_a": "两条",
        "option_b": "六条",
        "option_c": "四条",
        "option_d": "八条",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党纪律处分条例规定了对党员的几种纪律处分？",
        "option_a": "五种",
        "option_b": "六种",
        "option_c": "七种",
        "option_d": "八种",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党党员领导干部廉洁从政若干准则规定了多少条不准？",
        "option_a": "30条",
        "option_b": "52条",
        "option_c": "10条",
        "option_d": "8条",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的根本宗旨是由什么决定的？",
        "option_a": "党的路线",
        "option_b": "党的纲领",
        "option_c": "党的性质",
        "option_d": "党的政策",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的初心和使命是由什么决定的？",
        "option_a": "党的性质和宗旨",
        "option_b": "党的纲领和路线",
        "option_c": "党的历史和传统",
        "option_d": "党的理论和政策",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的最高领导机关是党的全国代表大会和它所产生的？",
        "option_a": "中央纪律检查委员会",
        "option_b": "中央政治局",
        "option_c": "中央政治局常务委员会",
        "option_d": "中央委员会",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的中央委员会总书记由什么会议选举产生？",
        "option_a": "中央委员会全体会议",
        "option_b": "中央政治局会议",
        "option_c": "中央政治局常务委员会会议",
        "option_d": "党的全国代表大会",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的中央军事委员会组成人员由什么会议决定？",
        "option_a": "中央政治局",
        "option_b": "中央委员会",
        "option_c": "中央政治局常务委员会",
        "option_d": "党的全国代表大会",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的地方各级委员会每届任期多久？",
        "option_a": "三年",
        "option_b": "四年",
        "option_c": "五年",
        "option_d": "六年",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的地方各级代表大会每几年举行一次？",
        "option_a": "五年",
        "option_b": "四年",
        "option_c": "三年",
        "option_d": "六年",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的基层组织，根据工作需要和党员人数，经上级党组织批准，分别设立党的基层委员会、总支部委员会、支部委员会，其中，党员人数超过多少人的基层单位，经上级党组织批准，可以设立党的基层委员会？",
        "option_a": "30人",
        "option_b": "50人",
        "option_c": "100人",
        "option_d": "20人",
        "correct_answer": "C",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的基层组织的基本任务不包括下列哪一项？",
        "option_a": "宣传和执行党的路线、方针、政策",
        "option_b": "组织党员认真学习马克思列宁主义、毛泽东思想、邓小平理论、‘三个代表’重要思想、科学发展观、习近平新时代中国特色社会主义思想",
        "option_c": "对党员进行教育、管理、监督和服务，提高党员素质，坚定理想信念，增强党性",
        "option_d": "制定党的路线、方针、政策",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的纪律检查机关是党的各级纪律检查委员会，它的主要任务是维护党的章程和其他党内法规，检查党的路线、方针、政策和决议的执行情况，协助党的委员会推进全面从严治党、加强党风建设和？",
        "option_a": "组织协调反腐败工作",
        "option_b": "开展反腐败斗争",
        "option_c": "查处腐败案件",
        "option_d": "预防腐败工作",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的纪律检查委员会的领导体制是？",
        "option_a": "垂直领导体制",
        "option_b": "双重领导体制",
        "option_c": "地方党委领导体制",
        "option_d": "上级纪委领导体制",
        "correct_answer": "B",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的纪律检查机关对党组织和党员领导干部履行职责、行使权力进行监督，受理处置党员群众检举举报，开展？",
        "option_a": "执纪问责",
        "option_b": "纪律审查",
        "option_c": "监察调查",
        "option_d": "谈话提醒、批评教育、诫勉谈话",
        "correct_answer": "D",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的纪律检查机关对违反党章和其他党内法规的党组织和党员，按照规定程序作出？",
        "option_a": "纪律处分决定或者提出纪律检查建议",
        "option_b": "组织处理决定",
        "option_c": "监察建议",
        "option_d": "问责决定",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "中国共产党的纪律检查机关发现同级党的委员会委员有违犯党的纪律的行为，可以先进行初步核实，如果需要立案检查的，应当在向同级党的委员会报告的同时向上一级纪律检查委员会报告；涉及常务委员的，报告上一级纪律检查委员会，由上一级纪律检查委员会进行？",
        "option_a": "初步核实",
        "option_b": "立案检查",
        "option_c": "调查取证",
        "option_d": "纪律处分",
        "correct_answer": "A",
        "difficulty": 1
    },
    {
        "question_text": "毛泽东在《论持久战》中科学地预见了抗日战争的三个阶段，下列哪个不属于这三个阶段？",
        "option_a": "战略防御阶段",
        "option_b": "战略相持阶段",
        "option_c": "战略反攻阶段",
        "option_d": "战略决战阶段",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "1945年党的七大确立的党的指导思想是？",
        "option_a": "马克思列宁主义",
        "option_b": "毛泽东思想",
        "option_c": "邓小平理论",
        "option_d": "实事求是思想路线",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "新中国成立初期，党领导人民进行的三大运动不包括下列哪一项？",
        "option_a": "土地改革",
        "option_b": "抗美援朝",
        "option_c": "镇压反革命",
        "option_d": "三反五反",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "1956年党的八大提出的我国社会主要矛盾是？",
        "option_a": "无产阶级和资产阶级的矛盾",
        "option_b": "社会主义道路和资本主义道路的矛盾",
        "option_c": "人民对于经济文化迅速发展的需要同当前经济文化不能满足人民需要的状况之间的矛盾",
        "option_d": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "‘两弹一星’中的‘两弹’指的是？",
        "option_a": "原子弹、氢弹",
        "option_b": "原子弹、导弹",
        "option_c": "氢弹、导弹",
        "option_d": "核弹、导弹",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "1978年真理标准问题大讨论的核心内容是？",
        "option_a": "实践是检验真理的唯一标准",
        "option_b": "解放思想、实事求是",
        "option_c": "改革开放",
        "option_d": "以经济建设为中心",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十一届三中全会作出的历史性决策是？",
        "option_a": "提出社会主义初级阶段理论",
        "option_b": "建立社会主义市场经济体制",
        "option_c": "把党和国家工作中心转移到经济建设上来、实行改革开放",
        "option_d": "确立邓小平理论为党的指导思想",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "1992年邓小平南方谈话中提出的著名论断不包括下列哪一项？",
        "option_a": "社会主义本质是解放和发展生产力",
        "option_b": "三个有利于标准",
        "option_c": "计划和市场都是经济手段",
        "option_d": "科学技术是第一生产力",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的十四大明确我国经济体制改革的目标是？",
        "option_a": "建立社会主义市场经济体制",
        "option_b": "完善社会主义计划经济体制",
        "option_c": "实行家庭联产承包责任制",
        "option_d": "建立现代企业制度",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "‘三个代表’重要思想首次提出的时间是？",
        "option_a": "1997年",
        "option_b": "2000年",
        "option_c": "2002年",
        "option_d": "2007年",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "科学发展观提出的根本依据是？",
        "option_a": "我国社会主义初级阶段基本国情",
        "option_b": "当前我国发展的阶段性特征",
        "option_c": "当代世界发展实践和发展理念",
        "option_d": "马克思主义关于发展的世界观和方法论",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十七大报告指出，新时期最鲜明的特点是？",
        "option_a": "改革开放",
        "option_b": "快速发展",
        "option_c": "与时俱进",
        "option_d": "实事求是",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "习近平新时代中国特色社会主义思想回答的重大时代课题是？",
        "option_a": "什么是社会主义、怎样建设社会主义",
        "option_b": "建设什么样的党、怎样建设党",
        "option_c": "实现什么样的发展、怎样发展",
        "option_d": "新时代坚持和发展什么样的中国特色社会主义、怎样坚持和发展中国特色社会主义",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，我国社会主要矛盾的变化，没有改变我们对我国社会主义所处历史阶段的判断，我国仍处于并将长期处于？",
        "option_a": "社社会主义高级阶段",
        "option_b": "社会主义中级阶段",
        "option_c": "会主义初级阶段",
        "option_d": "共产主义初级阶段",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "‘四个全面’战略布局中，全面深化改革的总目标是？",
        "option_a": "完善和发展中国特色社会主义制度、推进国家治理体系和治理能力现代化",
        "option_b": "建设中国特色社会主义法治体系、建设社会主义法治国家",
        "option_c": "建设一支听党指挥、能打胜仗、作风优良的人民军队",
        "option_d": "实现社会主义现代化和中华民族伟大复兴",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "全面依法治国的总目标是？",
        "option_a": "完善和发展中国特色社会主义制度、推进国家治理体系和治理能力现代化",
        "option_b": "建设中国特色社会主义法治体系、建设社会主义法治国家",
        "option_c": "坚持党的领导、人民当家作主、依法治国有机统一",
        "option_d": "科学立法、严格执法、公正司法、全民守法",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分中，撤销党内职务处分是指？",
        "option_a": "撤撤销受处分党员的行政职务",
        "option_b": "撤销受处分党员的一切职务",
        "option_c": "销受处分党员由党内选举或者组织任命的党内职务",
        "option_d": "撤销受处分党员的党内外一切职务",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视组对巡视对象执行《中国共产党章程》和其他党内法规，遵守党的纪律，落实全面从严治党主体责任和监督责任等情况进行监督，着力发现党的领导弱化、党的建设缺失、全面从严治党不力，党的观念淡漠、组织涣散、纪律松弛，管党治党宽松软问题，以及？",
        "option_a": "选人用人上的不正之风和腐败问题",
        "option_b": "违反中央八项规定精神问题",
        "option_c": "违反政治纪律和政治规矩、廉洁纪律、组织纪律、群众纪律、工作纪律、生活纪律等问题",
        "option_d": "落实意识形态工作责任制不到位问题",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活的基本制度不包括下列哪一项？",
        "option_a": "‘三会一课’制度",
        "option_b": "民主生活会和组织生活会制度",
        "option_c": "谈心谈话制度",
        "option_d": "领导干部个人有关事项报告制度",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "‘两学一做’学习教育常态化制度化的基本目标是？",
        "option_a": "教育引导党员做到政治合格、执行纪律合格、品德合格、发挥作用合格",
        "option_b": "推动全面从严治党向基层延伸",
        "option_c": "巩固拓展党的群众路线教育实践活动和‘三严三实’专题教育成果",
        "option_d": "增强党内政治生活的政治性、时代性、原则性、战斗性",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要以党的政治建设为统领，全面推进党的政治建设、思想建设、组织建设、作风建设、纪律建设，把什么贯穿其中？",
        "option_a": "文化建设",
        "option_b": "制度建设",
        "option_c": "反腐倡廉建设",
        "option_d": "能力建设",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党廉洁自律准则对党员领导干部提出的‘四个自觉’不包括下列哪一项？",
        "option_a": "廉洁从政，自觉保持人民公仆本色",
        "option_b": "廉洁用权，自觉维护人民根本利益",
        "option_c": "廉洁修身，自觉提升思想道德境界",
        "option_d": "廉洁齐家，自觉带头树立良好家风",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，对严重违犯党纪的党组织的纪律处理措施包括？",
        "option_a": "开除党籍",
        "option_b": "警告和严重警告",
        "option_c": "撤销党内职务和留党察看",
        "option_d": "改组和解散",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，党内监督的重点对象是？",
        "option_a": "党的领导机关和领导干部特别是主要领导干部",
        "option_b": "全体党员",
        "option_c": "党的基层组织",
        "option_d": "党员领导干部",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的群众路线教育实践活动的主要任务是集中解决形式主义、官僚主义、享乐主义和？",
        "option_a": "宗派主义",
        "option_b": "拜金主义",
        "option_c": "个人主义",
        "option_d": "奢靡之风",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "‘三严三实’专题教育中的‘三实’是指谋事要实、创业要实和？",
        "option_a": "做人要实",
        "option_b": "做事要实",
        "option_c": "说话要实",
        "option_d": "工作要实",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作的基本原则不包括下列哪一项？",
        "option_a": "坚持中央统一领导、分级负责",
        "option_b": "坚持实事求是、依法依规",
        "option_c": "坚持群众路线、发扬民主",
        "option_d": "坚持问题导向、注重实效",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，我国经济已由高速增长阶段转向什么阶段？",
        "option_a": "高质量发展阶段",
        "option_b": "中高速增长阶段",
        "option_c": "中低速增长阶段",
        "option_d": "低速增长阶段",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "新时代坚持和发展中国特色社会主义的基本方略共有多少条？",
        "option_a": "8条",
        "option_b": "10条",
        "option_c": "14条",
        "option_d": "6条",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "‘一带一路’倡议的核心理念是？",
        "option_a": "共商共建共享",
        "option_b": "互利共赢",
        "option_c": "开放包容",
        "option_d": "和平发展",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十九届四中全会审议通过的《中共中央关于坚持和完善中国特色社会主义制度、推进国家治理体系和治理能力现代化若干重大问题的决定》指出，我国国家制度和国家治理体系的显著优势共有多少个方面？",
        "option_a": "10个",
        "option_b": "13个",
        "option_c": "8个",
        "option_d": "5个",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党章程规定，党的基层委员会、总支部委员会、支部委员会每届任期？",
        "option_a": "三年至五年",
        "option_b": "两年至三年",
        "option_c": "五年",
        "option_d": "三年",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律检查委员会的主要任务不包括下列哪一项？",
        "option_a": "维护党的章程和其他党内法规",
        "option_b": "检查党的路线、方针、政策和决议的执行情况",
        "option_c": "协助党的委员会推进全面从严治党、加强党风建设和组织协调反腐败工作",
        "option_d": "制定党的路线、方针、政策",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员享有的各项权利必须受到尊重和保护，党的任何一级组织、任何党员都无权剥夺。党员应当增强党的观念和主体意识，将行使党章规定的权利作为对党应尽的责任，向党组织讲真话、讲实话、讲心里话，敢于担当、敢于负责，遵守纪律规矩，正确行使权利。这体现了党员权利保障的什么原则？",
        "option_a": "坚持民主和集中相结合",
        "option_b": "坚持权利和义务相统一",
        "option_c": "坚持在党的纪律面前人人平等",
        "option_d": "坚持依规依纪保障党员权利",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的组织原则民主集中制的基本原则不包括下列哪一项？",
        "option_a": "党员个人服从党的组织，少数服从多数，下级组织服从上级组织，全党各个组织和全体党员服从党的全国代表大会和中央委员会",
        "option_b": "党的各级领导机关，除它们派出的代表机关和在非党组织中的党组外，都由选举产生",
        "option_c": "党的最高领导机关，是党的全国代表大会和它所产生的中央委员会。党的地方各级领导机关，是党的地方各级代表大会和它们所产生的委员会。党的各级委员会向同级的代表大会负责并报告工作",
        "option_d": "党禁止任何形式的个人崇拜。要保证党的领导人的活动处于党和人民的监督之下，同时维护一切代表党和人民利益的领导人的威信",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视组实行组长负责制，副组长协助组长开展工作。巡视组组长根据什么确定并授权？",
        "option_a": "每次巡视任务",
        "option_b": "巡视地区或单位",
        "option_c": "巡视对象级别",
        "option_d": "巡视组规模",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要把党的政治建设摆在首位，党的政治建设的首要任务是？",
        "option_a": "发展积极健康的党内政治文化",
        "option_b": "严肃党内政治生活",
        "option_c": "保证全党服从中央，坚持党中央权威和集中统一领导",
        "option_d": "营造风清气正的良好政治生态",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党纪律处分条例规定，对于应当受到撤销党内职务处分，但是本人没有担任党内职务的，应当给予其什么处分？",
        "option_a": "严重警告处分",
        "option_b": "留党察看处分",
        "option_c": "开除党籍处分",
        "option_d": "警告处分",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的主要内容不包括下列哪一项？",
        "option_a": "学习党的基本理论、路线、方针、政策",
        "option_b": "开展批评与自我批评",
        "option_c": "讨论决定本地区本部门本单位的重大问题",
        "option_d": "汇报思想、工作和学习情况",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "‘不忘初心、牢记使命’主题教育的根本任务是？",
        "option_a": "深入学习贯彻习近平新时代中国特色社会主义思想，锤炼忠诚干净担当的政治品格，团结带领全国各族人民为实现伟大梦想共同奋斗",
        "option_b": "守初心、担使命，找差距、抓落实",
        "option_c": "实现中华民族伟大复兴的中国梦",
        "option_d": "全面建成小康社会",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，党内监督必须把纪律挺在前面，运用监督执纪‘四种形态’，经常开展批评和自我批评、约谈函询，让‘红红脸、出出汗’成为常态；党纪轻处分、组织调整成为违纪处理的大多数；党纪重处分、重大职务调整的成为少数；严重违纪涉嫌违法立案审查的成为极少数。这体现了党内监督的什么原则？",
        "option_a": "惩前毖后、治病救人",
        "option_b": "抓早抓小、防微杜渐",
        "option_c": "依规依纪、实事求是",
        "option_d": "民主集中制",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持党管干部原则，坚持德才兼备、以德为先，坚持五湖四海、任人唯贤，坚持事业为上、公道正派，把好干部标准落到实处。下列哪一项不属于好干部标准？",
        "option_a": "信念坚定、为民服务",
        "option_b": "勤政务实、敢于担当",
        "option_c": "清正廉洁、作风优良",
        "option_d": "勇于创新、善于学习",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党廉洁自律准则对党员提出的‘四个坚持’不包括下列哪一项？",
        "option_a": "坚持公私分明，先公后私，克己奉公",
        "option_b": "坚持崇廉拒腐，清白做人，干净做事",
        "option_c": "坚持尚俭戒奢，艰苦朴素，勤俭节约",
        "option_d": "坚持吃苦在前，享受在后，甘于奉献",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，留党察看处分分为留党察看一年、留党察看二年。对于受到留党察看处分一年的党员，期满后仍不符合恢复党员权利条件的，应当延长一年留党察看期限。留党察看期限最长不得超过？",
        "option_a": "二年",
        "option_b": "三年",
        "option_c": "四年",
        "option_d": "五年",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视工作人员实行任职回避、地域回避、公务回避。这体现了巡视工作的什么原则？",
        "option_a": "实事求是、依法依规",
        "option_b": "客观公正、廉洁自律",
        "option_c": "群众路线、发扬民主",
        "option_d": "严格保密、规范管理",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要以提升组织力为重点，突出政治功能，把企业、农村、机关、学校、科研院所、街道社区、社会组织等基层党组织建设成为宣传党的主张、贯彻党的决定、领导基层治理、团结动员群众、推动改革发展的坚强战斗堡垒。这体现了党的基层组织建设的什么要求？",
        "option_a": "组织建设",
        "option_b": "思想建设",
        "option_c": "政治建设",
        "option_d": "作风建设",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员有党内知情权，有权按照规定参加党的有关会议、阅读党的有关文件，了解党的路线方针政策和决议、党内事务及所处党组织的工作情况。这体现了党员的什么权利？",
        "option_a": "知情权",
        "option_b": "参与权",
        "option_c": "表达权",
        "option_d": "监督权",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，对于严重违犯党纪、本身又不能纠正的党组织领导机构，应当予以改组。受到改组处理的党组织领导机构成员，除应当受到撤销党内职务以上（含撤销党内职务）处分的外，均？",
        "option_a": "继续留任",
        "option_b": "自然免职",
        "option_c": "降职使用",
        "option_d": "另行安排工作",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，各级党组织应当把信任激励同严格监督结合起来，促使党的领导干部做到有权必有责、有责要担当，用权受监督、失责必追究。这体现了党内监督的什么原则？",
        "option_a": "抓早抓小、防微杜渐",
        "option_b": "惩前毖后、治病救人",
        "option_c": "权责对等、失责必究",
        "option_d": "依规依纪、实事求是",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要深化国家监察体制改革，将试点工作在全国推开，组建国家、省、市、县监察委员会，同党的纪律检查机关合署办公，实现对所有行使公权力的公职人员监察全覆盖。这体现了全面从严治党的什么要求？",
        "option_a": "全面覆盖",
        "option_b": "严字当头",
        "option_c": "标本兼治",
        "option_d": "以上率下",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视组可以采取的工作方式不包括下列哪一项？",
        "option_a": "听取被巡视党组织的工作汇报和有关部门的专题汇报",
        "option_b": "与被巡视党组织领导班子成员和其他干部群众进行个别谈话",
        "option_c": "查阅、复制有关文件、档案、会议记录等资料",
        "option_d": "对被巡视地区（单位）的党委（党组）主要负责人进行问责",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会一般多久召开一次？",
        "option_a": "每季度或每半年召开一次",
        "option_b": "每月召开一次",
        "option_c": "每年召开一次",
        "option_d": "每两年召开一次",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "‘不忘初心、牢记使命’主题教育的具体目标是理论学习有收获、思想政治受洗礼、干事创业敢担当、为民服务解难题和？",
        "option_a": "能力素质有提升",
        "option_b": "作风建设有成效",
        "option_c": "清正廉洁作表率",
        "option_d": "工作业绩有突破",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员有党内申诉权，对于党组织给予本人的处分、鉴定、审查结论或者其他处理不服的，有权向本人所在党组织、上级党组织直至中央提出申诉。这体现了党员的什么权利？",
        "option_a": "申诉权",
        "option_b": "控告权",
        "option_c": "辩护权",
        "option_d": "复议权",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，对于全体或者多数党员严重违犯党纪的党组织，应当予以解散。对于受到解散处理的党组织中的党员，应当逐个审查。其中，符合党员条件的，应当重新登记，并参加新的组织过党的生活；不符合党员条件的，应当对其进行教育、限期改正，经教育仍无转变的，予以？",
        "option_a": "开除党籍处分",
        "option_b": "留党察看处分",
        "option_c": "劝退或除名",
        "option_d": "撤销党内职务处分",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，中央政治局委员应当严格执行中央八项规定，自觉参加双重组织生活，如实向党中央报告个人重要事项。这体现了党内监督的什么要求？",
        "option_a": "以上率下",
        "option_b": "全面覆盖",
        "option_c": "严字当头",
        "option_d": "标本兼治",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持无禁区、全覆盖、零容忍，坚持重遏制、强高压、长震慑，坚持受贿行贿一起查，坚决防止党内形成利益集团。这体现了反腐败斗争的什么方针？",
        "option_a": "标本兼治、综合治理、惩防并举、注重预防",
        "option_b": "一体推进不敢腐、不能腐、不想腐",
        "option_c": "有案必查、违纪必究、执纪必严",
        "option_d": "抓早抓小、防微杜渐",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视工作领导小组的职责不包括下列哪一项？",
        "option_a": "贯彻党的中央委员会和同级党的委员会有关决议、决定",
        "option_b": "研究提出巡视工作规划、年度计划和阶段任务安排",
        "option_c": "听取巡视工作汇报",
        "option_d": "对被巡视党组织领导班子及其成员进行问责",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的程序一般不包括下列哪一项？",
        "option_a": "会前学习研讨、征求意见、谈心谈话",
        "option_b": "会上通报上一次组织生活会整改措施落实情况和本次组织生活会征求意见情况",
        "option_c": "领导班子成员逐一发言，作自我批评，其他成员对其提出批评意见",
        "option_d": "对被批评的党员进行纪律处分",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "‘两学一做’学习教育的基本内容是学党章党规、学系列讲话和？",
        "option_a": "做合格党员",
        "option_b": "做优秀党员",
        "option_c": "做模范党员",
        "option_d": "做先进党员",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员有党内选举权和被选举权，有权参加党内选举，了解候选人情况，要求改变候选人、不选任何一个候选人和另选他人。这体现了党员的什么权利？",
        "option_a": "参与权",
        "option_b": "选举权和被选举权",
        "option_c": "表达权",
        "option_d": "监督权",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，党员受到开除党籍处分，几年内不得重新入党？",
        "option_a": "三年内",
        "option_b": "五年内",
        "option_c": "二年内",
        "option_d": "一年内",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，党的基层组织应当发挥战斗堡垒作用，履行的监督职责不包括下列哪一项？",
        "option_a": "严格党的组织生活，开展批评和自我批评，监督党员切实履行义务，保障党员权利不受侵犯",
        "option_b": "了解党员、群众对党的工作和党的领导干部的批评和意见，定期向上级党组织反映情况，提出意见和建议",
        "option_c": "维护和执行党的纪律，发现党员、干部违反纪律问题及时教育或者处理，问题严重的应当向上级党组织报告",
        "option_d": "对上级党组织决议、决定贯彻执行情况进行监督",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要把坚定理想信念作为党的思想建设的首要任务，教育引导全党牢记党的宗旨，挺起共产党人的精神脊梁，解决好世界观、人生观、价值观这个‘总开关’问题。这体现了党的思想建设的什么要求？",
        "option_a": "补钙壮骨、立根固本",
        "option_b": "与时俱进、开拓创新",
        "option_c": "实事求是、求真务实",
        "option_d": "解放思想、实事求是",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视组对反映被巡视党组织领导班子及其成员的重要问题和线索，可以进行深入了解。这里的‘重要问题和线索’不包括下列哪一项？",
        "option_a": "违反政治纪律和政治规矩的问题",
        "option_b": "违反廉洁纪律的问题",
        "option_c": "工作中的一般性失误",
        "option_d": "选人用人上的不正之风和腐败问题",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的重要作用不包括下列哪一项？",
        "option_a": "加强党内监督",
        "option_b": "增进党内团结",
        "option_c": "提高党员素质",
        "option_d": "制定党的路线方针政策",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "‘不忘初心、牢记使命’主题教育的总要求是守初心、担使命和？",
        "option_a": "找差距、抓落实",
        "option_b": "学理论、强党性",
        "option_c": "转作风、树形象",
        "option_d": "重实践、求实效",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员有党内监督权，有权在党的会议上以口头或者书面方式有根据地批评党的任何组织和任何党员，揭露、要求纠正工作中存在的缺点、错误，对党的决议和政策提出意见和建议。这体现了党员的什么权利？",
        "option_a": "监督权",
        "option_b": "批评权",
        "option_c": "建议权",
        "option_d": "检举权",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，对于党员违犯党纪应当给予警告或者严重警告处分，但是具有本条例第十七条规定的情形之一或者本条例分则中另有规定的，可以给予批评教育、责令检查、诫勉或者组织处理，免予党纪处分。对违纪党员免予处分，应当作出书面结论。这里的‘第十七条规定的情形’不包括下列哪一项？",
        "option_a": "主动交代本人应当受到党纪处分的问题的",
        "option_b": "在组织核实、立案审查过程中，能够配合核实审查工作，如实说明本人违纪违法事实的",
        "option_c": "检举同案人或者其他人应当受到党纪处分或者法律追究的问题，经查证属实的",
        "option_d": "主动挽回损失、消除不良影响或者有效阻止危害结果发生的",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，党员应当本着对党和人民事业高度负责的态度，积极行使党员权利，履行的监督义务不包括下列哪一项？",
        "option_a": "加强对党的领导干部的民主监督，及时向党组织反映群众意见和诉求",
        "option_b": "在党的会议上有根据地批评党的任何组织和任何党员，揭露和纠正工作中的缺点、错误",
        "option_c": "参加党组织开展的评议领导干部活动，勇于触及矛盾问题、指出缺点错误，对错误言行敢于较真、敢于斗争",
        "option_d": "对同级党组织的决议、决定提出批评和建议",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持党对一切工作的领导。党政军民学，东西南北中，党是领导一切的。必须增强政治意识、大局意识、核心意识、看齐意识，自觉维护党中央权威和集中统一领导，自觉在思想上政治上行动上同党中央保持高度一致。这体现了党的什么原则？",
        "option_a": "坚持党对一切工作的领导",
        "option_b": "坚持以人民为中心",
        "option_c": "坚持全面深化改革",
        "option_d": "坚持新发展理念",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，被巡视党组织收到巡视组反馈意见后，应当认真整改落实，并于几个月内将整改情况报告和主要负责人组织落实情况报告，报送巡视工作领导小组办公室？",
        "option_a": "3个月内",
        "option_b": "1个月内",
        "option_c": "2个月内",
        "option_d": "6个月内",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的参加人员不包括下列哪一项？",
        "option_a": "党支部全体党员",
        "option_b": "上级党组织派人参加",
        "option_c": "入党积极分子",
        "option_d": "预备党员",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "‘两学一做’学习教育的目标是进一步解决党员队伍在思想、组织、作风、纪律等方面存在的问题，保持发展党的先进性和？",
        "option_a": "纯洁性",
        "option_b": "战斗性",
        "option_c": "革命性",
        "option_d": "时代性",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员有党内请求权，有权向所在党组织、上级党组织直至中央提出请求。这里的‘请求’不包括下列哪一项？",
        "option_a": "请求党组织给予帮助解决个人困难",
        "option_b": "请求党组织给予本人表扬奖励",
        "option_c": "请求党组织对本人作出处分决定进行复议、复查",
        "option_d": "请求党组织保护本人的民主权利和合法权益",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，党员受到留党察看处分，其党内职务自然撤销。对于担任党外职务的，应当建议党外组织撤销其党外职务。受到留党察看处分的党员，恢复党员权利后几年内，不得在党内担任和向党外组织推荐担任与其原任职务相当或者高于其原任职务的职务？",
        "option_a": "二年内",
        "option_b": "三年内",
        "option_c": "五年内",
        "option_d": "一年内",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，各级纪律检查机关必须加强自身建设，健全内控机制，自觉接受党内监督、社会监督、群众监督，确保权力受到严格约束。这体现了纪检机关的什么要求？",
        "option_a": "客观公正、廉洁自律",
        "option_b": "实事求是、依法依规",
        "option_c": "严格保密、规范管理",
        "option_d": "忠诚干净担当",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持全面从严治党，必须以党章为根本遵循，把党的政治建设摆在首位，思想建党和制度治党同向发力，统筹推进党的各项建设，抓住‘关键少数’，坚持‘三严三实’，坚持民主集中制，严肃党内政治生活，严明党的纪律，强化党内监督，发展积极健康的党内政治文化，全面净化党内政治生态，坚决纠正各种不正之风，以零容忍态度惩治腐败。这体现了全面从严治党的什么要求？",
        "option_a": "惩防并举、注重预防",
        "option_b": "标本兼治、综合治理",
        "option_c": "严字当头、全面从严",
        "option_d": "以上率下、层层传导",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视工作人员应当具备的基本条件不包括下列哪一项？",
        "option_a": "理想信念坚定，对党忠诚，在思想上政治上行动上同党中央保持高度一致",
        "option_b": "坚持原则，敢于担当，依法办事，公道正派，清正廉洁",
        "option_c": "熟悉党务工作和相关政策法规，具有较强的发现问题、沟通协调、文字综合等能力",
        "option_d": "具有博士以上学历",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的主题一般由谁确定？",
        "option_a": "上级党组织根据实际情况确定，或者由党支部根据上级党组织的要求和本支部的实际情况确定",
        "option_b": "党支部书记个人确定",
        "option_c": "党支部委员会集体研究确定",
        "option_d": "全体党员投票确定",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "‘不忘初心、牢记使命’主题教育的四个贯穿始终是学习教育、调查研究、检视问题和？",
        "option_a": "征求意见",
        "option_b": "整改落实",
        "option_c": "谈心谈话",
        "option_d": "民主评议",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员有党内申辩权，有权在党组织讨论决定对本人的党纪处分或者作出鉴定时，进行申辩，其他党员可以为其作证和辩护。这体现了党员的什么权利？",
        "option_a": "申诉权",
        "option_b": "辩护权",
        "option_c": "申辩权",
        "option_d": "作证权",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，对于在党内担任两个以上职务的党员，党组织在作处分决定时，应当明确是撤销其一切职务还是某个职务。如果决定撤销其某个职务，必须撤销其担任的最高职务。如果决定撤销其两个以上职务，则必须从其担任的最高职务开始依次撤销。对于在党外组织担任职务的，应当建议党外组织依照规定作出相应处理。这体现了纪律处分的什么原则？",
        "option_a": "实事求是、依规依纪",
        "option_b": "惩前毖后、治病救人",
        "option_c": "纪律面前人人平等",
        "option_d": "民主集中制",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，中央政治局常务委员会应当加强对中央政治局工作的监督，定期研究部署在全党开展学习教育，以整风精神查找问题、纠正偏差。这体现了党内监督的什么要求？",
        "option_a": "以上率下",
        "option_b": "全面覆盖",
        "option_c": "严字当头",
        "option_d": "标本兼治",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持新发展理念，必须坚定不移贯彻创新、协调、绿色、开放、共享的发展理念。其中，共享发展注重的是解决什么问题？",
        "option_a": "社会公平正义问题",
        "option_b": "发展不平衡问题",
        "option_c": "人与自然和谐共生问题",
        "option_d": "发展动力问题",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视工作领导小组办公室的职责不包括下列哪一项？",
        "option_a": "向巡视工作领导小组报告工作情况，传达贯彻巡视工作领导小组的决策和部署",
        "option_b": "统筹、协调、指导巡视组开展工作",
        "option_c": "对被巡视党组织领导班子及其成员进行问责",
        "option_d": "承担政策研究、制度建设等工作",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的批评与自我批评应当坚持的原则不包括下列哪一项？",
        "option_a": "实事求是、出于公心、与人为善",
        "option_b": "敢于揭短亮丑、真刀真枪、见筋见骨",
        "option_c": "坚持‘团结—批评—团结’的方针",
        "option_d": "只批评别人，不自我批评",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "‘两学一做’学习教育的学习内容不包括下列哪一项？",
        "option_a": "学习马克思列宁主义、毛泽东思想、邓小平理论、‘三个代表’重要思想、科学发展观",
        "option_b": "学习习近平总书记系列重要讲话精神",
        "option_c": "学习党的历史、革命先辈和先进典型",
        "option_d": "学习业务知识和专业技能",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员有党内提出罢免撤换要求权，有权向所在党组织或者上级党组织反映领导干部不称职的情况，要求罢免或者撤换不称职的领导干部。这体现了党员的什么权利？",
        "option_a": "罢免权",
        "option_b": "监督权",
        "option_c": "建议权",
        "option_d": "控告权",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，党员受到警告处分一年内、受到严重警告处分一年半内，不得在党内提升职务和向党外组织推荐担任高于其原任职务的党外职务。这体现了纪律处分的什么作用？",
        "option_a": "惩戒作用",
        "option_b": "教育作用",
        "option_c": "震慑作用",
        "option_d": "预防作用",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，各级党组织应当把信任激励同严格监督结合起来，促使党的领导干部做到有权必有责、有责要担当，用权受监督、失责必追究。这体现了党内监督的什么原则？",
        "option_a": "抓早抓小、防微杜渐",
        "option_b": "惩前毖后、治病救人",
        "option_c": "权责对等、失责必究",
        "option_d": "依规依纪、实事求是",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持全面深化改革，必须坚持和完善中国特色社会主义制度，不断推进国家治理体系和治理能力现代化，坚决破除一切不合时宜的思想观念和体制机制弊端，突破利益固化的藩篱，吸收人类文明有益成果，构建系统完备、科学规范、运行有效的制度体系。这体现了全面深化改革的什么要求？",
        "option_a": "系统性、整体性、协同性",
        "option_b": "问题导向、目标导向、结果导向",
        "option_c": "摸着石头过河和顶层设计相结合",
        "option_d": "胆子要大、步子要稳",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视组应当严格执行请示报告制度，对巡视工作中的重要情况和重大问题及时向巡视工作领导小组请示报告。这里的‘重要情况和重大问题’不包括下列哪一项？",
        "option_a": "被巡视党组织领导班子成员涉嫌严重违纪违法问题",
        "option_b": "被巡视地区（单位）发生的重大突发事件",
        "option_c": "巡视工作人员违反工作纪律和廉洁纪律问题",
        "option_d": "被巡视党组织的日常工作情况",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的整改措施应当做到的‘三个明确’不包括下列哪一项？",
        "option_a": "明确整改事项",
        "option_b": "明确整改措施",
        "option_c": "明确整改责任人和完成时限",
        "option_d": "明确整改资金",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "‘不忘初心、牢记使命’主题教育的学习重点是深入学习贯彻？",
        "option_a": "党章党规",
        "option_b": "习近平新时代中国特色社会主义思想",
        "option_c": "党的十九大报告",
        "option_d": "习近平总书记系列重要讲话精神",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，对于党员的申诉，有关党组织应当按照规定进行复议、复查，不得扣压。上级党组织认为必要时，可以直接或者指定有关党组织进行复议、复查。这体现了党员权利保障的什么原则？",
        "option_a": "坚持民主集中制",
        "option_b": "实事求是、依规依纪",
        "option_c": "保障党员权利不受侵犯",
        "option_d": "及时受理、认真办理",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，党组织在纪律审查中发现党员有贪污贿赂、滥用职权、玩忽职守、权力寻租、利益输送、徇私舞弊、浪费国家资财等违反法律涉嫌犯罪行为的，应当给予撤销党内职务、留党察看或者开除党籍处分。这体现了纪律处分的什么原则？",
        "option_a": "惩前毖后、治病救人",
        "option_b": "实事求是、依规依纪",
        "option_c": "纪律面前人人平等",
        "option_d": "纪严于法、纪在法前",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，党内监督的任务是确保党章党规党纪在全党有效执行，维护党的团结统一，重点解决党的领导弱化、党的建设缺失、全面从严治党不力，党的观念淡漠、组织涣散、纪律松弛，管党治党宽松软问题，保证党的组织充分履行职能、发挥核心作用，保证全体党员发挥先锋模范作用，保证党的领导干部忠诚干净担当。这体现了党内监督的什么目标？",
        "option_a": "坚持党的领导、加强党的建设、全面从严治党",
        "option_b": "维护党的团结统一",
        "option_c": "保证党的组织充分履行职能",
        "option_d": "保证全体党员发挥先锋模范作用",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持总体国家安全观，必须坚持国家利益至上，以人民安全为宗旨，以政治安全为根本，统筹外部安全和内部安全、国土安全和国民安全、传统安全和非传统安全、自身安全和共同安全，完善国家安全制度体系，加强国家安全能力建设，坚决维护国家主权、安全、发展利益。这体现了总体国家安全观的什么要求？",
        "option_a": "统筹发展和安全",
        "option_b": "以人民为中心",
        "option_c": "系统思维",
        "option_d": "底线思维",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视组进驻被巡视地区（单位）后，应当向被巡视党组织通报巡视任务，按照规定的工作方式和权限，开展巡视了解工作。这里的‘工作方式和权限’不包括下列哪一项？",
        "option_a": "对被巡视地区（单位）的党委（党组）主要负责人进行诫勉谈话",
        "option_b": "受理反映被巡视党组织领导班子及其成员和下一级党组织领导班子主要负责人问题的来信、来电、来访等",
        "option_c": "抽查核实领导干部报告个人有关事项的情况",
        "option_d": "向有关知情人询问情况",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的整改落实情况应当如何公开？",
        "option_a": "不需要公开",
        "option_b": "只在领导班子内部通报",
        "option_c": "在一定范围内通报，并接受党员和群众监督",
        "option_d": "只向上级党组织报告",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "‘两学一做’学习教育的基本单位是？",
        "option_a": "党支部",
        "option_b": "党小组",
        "option_c": "基层党委",
        "option_d": "党总支",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，对于有侵犯党员权利行为的党组织，上级党组织应当责令其改正；情节严重的，按照规定追究有关责任者的责任。对于有侵犯党员权利行为的党员，其所在党组织或者上级党组织可以采取责令停止侵权行为、责令赔礼道歉、责令作出检查、诫勉谈话、通报批评等方式给予处理；情节较重的，按照规定给予党纪处分。这体现了党员权利保障的什么措施？",
        "option_a": "责监督检查",
        "option_b": "权利救济",
        "option_c": "任追究",
        "option_d": "教育引导",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，党员受到党纪处分后，党组织应当按照干部管理权限和组织关系，将处分决定材料归入受处分者档案；对于受到撤销党内职务以上（含撤销党内职务）处分的，还应当在一个月内办理职务、工资等相应变更手续。特殊情况下，经作出或者批准作出处分决定的组织批准，可以适当延长办理期限。办理期限最长不得超过？",
        "option_a": "六个月",
        "option_b": "三个月",
        "option_c": "一年",
        "option_d": "两个月",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，党内监督的重点内容不包括下列哪一项？",
        "option_a": "遵守党章党规，坚定理想信念，践行党的宗旨，模范遵守宪法法律情况",
        "option_b": "维护党中央集中统一领导，牢固树立政治意识、大局意识、核心意识、看齐意识，贯彻落实党的理论和路线方针政策，确保全党令行禁止情况",
        "option_c": "坚持民主集中制，严肃党内政治生活，贯彻党员个人服从党的组织，少数服从多数，下级组织服从上级组织，全党各个组织和全体党员服从党的全国代表大会和中央委员会原则情况",
        "option_d": "党员个人的生活作风和家庭情况",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持党对人民军队的绝对领导，必须全面贯彻党对军队绝对领导的根本原则和制度，全面贯彻新时代党的强军思想，坚持政治建军、改革强军、科技兴军、依法治军，建设一支听党指挥、能打胜仗、作风优良的人民军队，把人民军队建设成为世界一流军队。这体现了党对军队绝对领导的什么要求？",
        "option_a": "改革强军",
        "option_b": "政治建军",
        "option_c": "科技兴军",
        "option_d": "依法治军",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，巡视组应当形成巡视报告，如实报告了解的重要情况和问题，并提出处理建议。巡视报告经巡视工作领导小组同意后，巡视组应当在几个工作日内向被巡视党组织领导班子反馈巡视情况，指出问题，有针对性地提出整改意见？",
        "option_a": "10个工作日内",
        "option_b": "15个工作日内",
        "option_c": "7个工作日内",
        "option_d": "5个工作日内",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的成功召开，关键在于？",
        "option_a": "领导带头、真批评、真整改",
        "option_b": "会议开得越长越好",
        "option_c": "参加人数越多越好",
        "option_d": "批评意见越多越好",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "‘不忘初心、牢记使命’主题教育的鲜明特点是？",
        "option_a": "以上率下、示范带动",
        "option_b": "全面覆盖、不留死角",
        "option_c": "问题导向、务求实效",
        "option_d": "学做结合、查改贯通",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党组织对党员作出处分决定所依据的事实材料和处分决定必须同本人见面，听取本人说明情况和申辩。对于党员的申辩及其他党员为其所作的证明和辩护，有关党组织要认真听取、如实记录，并进一步核实，采纳其合理意见；不予采纳的，要向本人说明理由。这体现了党员权利保障的什么原则？",
        "option_a": "坚持民主集中制",
        "option_b": "保障党员权利不受侵犯",
        "option_c": "及时受理、认真办理",
        "option_d": "实事求是、依规依纪",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，对于受到解散处理的党组织中的党员，应当逐个审查。其中，符合党员条件的，应当重新登记，并参加新的组织过党的生活；不符合党员条件的，应当对其进行教育、限期改正，经教育仍无转变的，予以劝退或除名。这体现了纪律处分的什么原则？",
        "option_a": "惩前毖后、治病救人",
        "option_b": "实事求是、依规依纪",
        "option_c": "纪律面前人人平等",
        "option_d": "民主集中制",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，党内监督必须把纪律挺在前面，运用监督执纪‘四种形态’，经常开展批评和自我批评、约谈函询，让‘红红脸、出出汗’成为常态；党纪轻处分、组织调整成为违纪处理的大多数；党纪重处分、重大职务调整的成为少数；严重违纪涉嫌违法立案审查的成为极少数。这体现了党内监督的什么策略？",
        "option_a": "抓早抓小、防微杜渐",
        "option_b": "惩前毖后、治病救人",
        "option_c": "依规依纪、实事求是",
        "option_d": "民主集中制",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持以人民为中心，必须坚持人民主体地位，坚持立党为公、执政为民，践行全心全意为人民服务的根本宗旨，把党的群众路线贯彻到治国理政全部活动之中，把人民对美好生活的向往作为奋斗目标，依靠人民创造历史伟业。这体现了党的什么根本立场？",
        "option_a": "国家立场",
        "option_b": "阶级立场",
        "option_c": "人民立场",
        "option_d": "民族立场",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党巡视工作条例规定，被巡视党组织收到巡视组反馈意见后，应当认真整改落实，并于2个月内将整改情况报告和主要负责人组织落实情况报告，报送巡视工作领导小组办公室。被巡视党组织主要负责人为落实整改工作的？",
        "option_a": "重要责任人",
        "option_b": "主要责任人",
        "option_c": "直接责任人",
        "option_d": "第一责任人",
        "correct_answer": "D",
        "difficulty": 2
    },
    {
        "question_text": "党的组织生活会的核心是？",
        "option_a": "学习党的理论",
        "option_b": "开展批评与自我批评",
        "option_c": "汇报工作情况",
        "option_d": "制定整改措施",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "‘两学一做’学习教育的基本方式是？",
        "option_a": "基础在学、关键在做",
        "option_b": "集中学习、专题研讨",
        "option_c": "个人自学、集体学习",
        "option_d": "理论学习、实践锻炼",
        "correct_answer": "A",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党员权利保障条例规定，党员有党内提出建议权，有权以口头或者书面方式对本地区本部门本单位的党组织、上级党组织直至中央的各方面工作提出建议和倡议。这体现了党员的什么权利？",
        "option_a": "表达权",
        "option_b": "参与权",
        "option_c": "建议权",
        "option_d": "监督权",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "党的纪律处分条例规定，党员受到党纪处分后，对于在党外组织担任职务的，应当建议党外组织依照规定作出相应处理。这体现了纪律处分的什么效力？",
        "option_a": "仅党外效力",
        "option_b": "仅党内效力",
        "option_c": "党内效力和党外建议效力",
        "option_d": "无党外效力",
        "correct_answer": "C",
        "difficulty": 2
    },
    {
        "question_text": "中国共产党党内监督条例规定，各级党组织应当把信任激励同严格监督结合起来，促使党的领导干部做到有权必有责、有责要担当，用权受监督、失责必追究。这体现了党内监督的什么目的？",
        "option_a": "惩治腐败",
        "option_b": "确保权力正确运行",
        "option_c": "加强党的领导",
        "option_d": "维护党的团结统一",
        "correct_answer": "B",
        "difficulty": 2
    },
    {
        "question_text": "党的十九大报告指出，要坚持新发展理念，必须坚定不移贯彻创新、协调、绿色、开放、共享的发展理念。其中，创新发展注重的是解决什么问题？",
        "option_a": "发展动力问题",
        "option_b": "发展不平衡问题",
        "option_c": "人与自然和谐共生问题",
        "option_d": "社会公平正义问题",
        "correct_answer": "A",
        "difficulty": 2
    },
            {
                "question_text": "毛泽东在《论持久战》中科学地预见了抗日战争将经过哪三个阶段？",
                "option_a": "战略防御、战略相持、战略反攻",
                "option_b": "战略进攻、战略防御、战略决战",
                "option_c": "战略相持、战略进攻、战略撤退",
                "option_d": "战略防御、战略反攻、战略决战",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "1945年党的七大确立的党的指导思想是什么？",
                "option_a": "马克思列宁主义",
                "option_b": "毛泽东思想",
                "option_c": "邓小平理论",
                "option_d": "三个代表重要思想",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "新中国成立初期，党领导开展的三大运动不包括下列哪一项？",
                "option_a": "土地改革运动",
                "option_b": "抗美援朝运动",
                "option_c": "镇压反革命运动",
                "option_d": "整风运动",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "1956年党的八大提出的我国社会主要矛盾是？",
                "option_a": "人民对于建立先进的工业国的要求同落后的农业国的现实之间的矛盾",
                "option_b": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾",
                "option_c": "无产阶级和资产阶级之间的矛盾",
                "option_d": "社会主义道路和资本主义道路之间的矛盾",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "‘两弹一星’中的‘两弹’指的是？",
                "option_a": "原子弹、氢弹",
                "option_b": "原子弹、导弹",
                "option_c": "氢弹、导弹",
                "option_d": "核弹、导弹",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "1978年5月11日，《光明日报》特约评论员文章《实践是检验真理的唯一标准》的发表，引发了全国范围的什么讨论？",
                "option_a": "思想解放大讨论",
                "option_b": "改革开放大讨论",
                "option_c": "真理标准问题大讨论",
                "option_d": "实事求是大讨论",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "党的十一届三中全会作出的历史性决策是？",
                "option_a": "确立邓小平理论为党的指导思想",
                "option_b": "建立社会主义市场经济体制",
                "option_c": "提出社会主义初级阶段理论",
                "option_d": "把党和国家工作中心转移到经济建设上来、实行改革开放",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "1982年党的十二大首次提出的重大命题是？",
                "option_a": "三个代表重要思想",
                "option_b": "社会主义初级阶段理论",
                "option_c": "社会主义市场经济理论",
                "option_d": "建设有中国特色的社会主义",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "我国对外开放的第一个经济特区是？",
                "option_a": "珠海",
                "option_b": "深圳",
                "option_c": "厦门",
                "option_d": "汕头",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "党的十三大系统阐述了社会主义初级阶段的理论，明确概括了党在社会主义初级阶段的？",
                "option_a": "基本路线",
                "option_b": "基本纲领",
                "option_c": "基本经验",
                "option_d": "基本方略",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "1992年邓小平南方谈话中，明确提出判断改革开放和各项工作得失的标准是？",
                "option_a": "是否有利于巩固党的领导，是否有利于社会主义制度的完善，是否有利于实现共同富裕",
                "option_b": "是否有利于发展社会主义社会的生产力，是否有利于增强社会主义国家的综合国力，是否有利于提高人民的生活水平",
                "option_c": "是否有利于经济发展，是否有利于社会稳定，是否有利于提高国际地位",
                "option_d": "是否有利于解放思想，是否有利于实事求是，是否有利于与时俱进",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "党的十四大明确我国经济体制改革的目标是建立？",
                "option_a": "社会主义市场经济体制",
                "option_b": "计划经济与市场经济相结合的体制",
                "option_c": "有计划的商品经济体制",
                "option_d": "社会主义商品经济体制",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "‘三个代表’重要思想首次提出的时间是？",
                "option_a": "2000年",
                "option_b": "2001年",
                "option_c": "2002年",
                "option_d": "1997年",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "党的十六大提出的全面建设小康社会的奋斗目标是到哪一年？",
                "option_a": "2050年",
                "option_b": "2035年",
                "option_c": "2020年",
                "option_d": "2010年",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "科学发展观首次提出的时间是？",
                "option_a": "2005年",
                "option_b": "2004年",
                "option_c": "2003年",
                "option_d": "2007年",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "党的十七大报告指出，科学发展观的核心是？",
                "option_a": "全面协调可持续",
                "option_b": "发展",
                "option_c": "以人为本",
                "option_d": "统筹兼顾",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "2012年党的十八大报告指出，建设中国特色社会主义总布局是？",
                "option_a": "五位一体",
                "option_b": "四位一体",
                "option_c": "三位一体",
                "option_d": "六位一体",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "党的十八大以来，以习近平同志为核心的党中央提出的‘四个全面’战略布局不包括下列哪一项？",
                "option_a": "全面建成小康社会",
                "option_b": "全面深化改革",
                "option_c": "全面依法治国",
                "option_d": "全面建设社会主义现代化国家",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "2013年11月，党的十八届三中全会通过的《中共中央关于全面深化改革若干重大问题的决定》指出，全面深化改革的总目标是？",
                "option_a": "建设社会主义市场经济体制",
                "option_b": "完善和发展中国特色社会主义制度，推进国家治理体系和治理能力现代化",
                "option_c": "实现社会主义现代化和中华民族伟大复兴",
                "option_d": "全面建成小康社会",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "2014年10月，党的十八届四中全会通过的《中共中央关于全面推进依法治国若干重大问题的决定》指出，全面推进依法治国的总目标是？",
                "option_a": "建设中国特色社会主义法治体系，建设社会主义法治国家",
                "option_b": "完善中国特色社会主义法律体系",
                "option_c": "推进科学立法、严格执法、公正司法、全民守法",
                "option_d": "坚持依法治国和以德治国相结合",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "‘两学一做’学习教育开始的时间是？",
                "option_a": "2015年",
                "option_b": "2016年",
                "option_c": "2017年",
                "option_d": "2014年",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "党的十九大报告指出，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和？",
                "option_a": "城乡发展差距之间的矛盾",
                "option_b": "落后的社会生产之间的矛盾",
                "option_c": "不平衡不充分的发展之间的矛盾",
                "option_d": "区域发展不平衡之间的矛盾",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "党的十九大报告指出，中国特色社会主义进入新时代，我国社会主要矛盾的变化？",
                "option_a": "没有改变我们对我国社会主义所处历史阶段的判断",
                "option_b": "改变了我们对我国社会主义所处历史阶段的判断",
                "option_c": "表明我国已经进入社会主义高级阶段",
                "option_d": "表明我国已经实现社会主义现代化",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "党的十九大报告指出，从2020年到2035年，在全面建成小康社会的基础上，再奋斗十五年，基本实现？",
                "option_a": "社会主义现代化",
                "option_b": "社会主义现代化强国",
                "option_c": "共同富裕",
                "option_d": "中华民族伟大复兴",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "党的十九大报告指出，从2035年到本世纪中叶，在基本实现现代化的基础上，再奋斗十五年，把我国建成？",
                "option_a": "富强民主文明和谐的社会主义现代化国家",
                "option_b": "富强民主文明和谐美丽的社会主义现代化强国",
                "option_c": "中等发达国家水平",
                "option_d": "全面小康社会",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "习近平新时代中国特色社会主义思想的核心内容是？",
                "option_a": "新发展理念",
                "option_b": "‘五位一体’总体布局和‘四个全面’战略布局",
                "option_c": "‘八个明确’和‘十四个坚持’",
                "option_d": "全面深化改革",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "党的十九届四中全会通过的《中共中央关于坚持和完善中国特色社会主义制度、推进国家治理体系和治理能力现代化若干重大问题的决定》指出，我国国家制度和国家治理体系的显著优势有多少个方面？",
                "option_a": "8个",
                "option_b": "10个",
                "option_c": "15个",
                "option_d": "13个",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "2020年，我国脱贫攻坚战取得全面胜利，现行标准下农村贫困人口全部脱贫，贫困县全部摘帽，历史性地解决了？",
                "option_a": "绝对贫困问题",
                "option_b": "相对贫困问题",
                "option_c": "贫困代际传递问题",
                "option_d": "区域性整体贫困问题",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "党的二十大报告指出，全面建设社会主义现代化国家的首要任务是？",
                "option_a": "高质量发展",
                "option_b": "共同富裕",
                "option_c": "科技创新",
                "option_d": "改革开放",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "党的二十大报告指出，中国式现代化的本质要求不包括下列哪一项？",
                "option_a": "坚持中国共产党领导",
                "option_b": "坚持中国特色社会主义",
                "option_c": "实现高质量发展",
                "option_d": "走和平发展道路",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党历史上的第一个中央纪律检查机构——中央监察委员会成立于哪次会议？",
                "option_a": "中共七大",
                "option_b": "中共六大",
                "option_c": "中共五大",
                "option_d": "中共八大",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "1935年1月召开的遵义会议集中解决了当时具有决定意义的？",
                "option_a": "军事问题和组织问题",
                "option_b": "政治路线问题",
                "option_c": "思想路线问题",
                "option_d": "作风建设问题",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "抗日战争时期，中国共产党在敌后抗日根据地实行的土地政策是？",
                "option_a": "减土地国有化",
                "option_b": "耕者有其田",
                "option_c": "租减息",
                "option_d": "土地集体化",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "1949年3月召开的党的七届二中全会，毛泽东提出的‘两个务必’是？",
                "option_a": "务必使同志们继续地保持谦虚、谨慎、不骄、不躁的作风，务必使同志们继续地保持艰苦奋斗的作风",
                "option_b": "务必坚持党的领导，务必坚持人民民主专政",
                "option_c": "务必坚持马克思主义，务必坚持社会主义道路",
                "option_d": "务必解放思想，务必实事求是",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "新中国成立初期，党领导的‘三反’运动是指反对贪污、反对浪费和反对？",
                "option_a": "形式主义",
                "option_b": "官僚主义",
                "option_c": "宗派主义",
                "option_d": "主观主义",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "1954年9月，第一届全国人民代表大会第一次会议通过的法律文件是？",
                "option_a": "《中华人民共和国土地改革法》",
                "option_b": "《中华人民共和国宪法》",
                "option_c": "《中华人民共和国婚姻法》",
                "option_d": "《中华人民共和国刑法》",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "1956年，我国对农业、手工业和资本主义工商业的社会主义改造基本完成，标志着？",
                "option_a": "社会主义制度在我国基本建立起来",
                "option_b": "我国进入社会主义初级阶段",
                "option_c": "我国实现了新民主主义向社会主义的过渡",
                "option_d": "以上都对",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "1978年党的十一届三中全会重新确立的思想路线是？",
                "option_a": "解放思想、实事求是",
                "option_b": "与时俱进、开拓创新",
                "option_c": "独立自主、自力更生",
                "option_d": "实事求是、群众路线",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "1987年党的十三大提出的社会主义初级阶段的基本路线可以概括为？",
                "option_a": "‘鼓足干劲，力争上游，多快好省地建设社会主义’",
                "option_b": "‘一化三改’",
                "option_c": "‘一个中心，两个基本点’",
                "option_d": "‘以阶级斗争为纲’",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "1992年党的十四大明确我国经济体制改革的目标是建立和完善？",
                "option_a": "社会主义市场经济体制",
                "option_b": "有计划的商品经济体制",
                "option_c": "计划经济与市场经济相结合的体制",
                "option_d": "社会主义商品经济体制",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "2000年2月，江泽民在广东考察时首次提出的重要思想是？",
                "option_a": "习近平新时代中国特色社会主义思想",
                "option_b": "科学发展观",
                "option_c": "社会主义荣辱观",
                "option_d": "三个代表重要思想",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "2003年10月，党的十六届三中全会明确提出的科学发展观的基本要求是？",
                "option_a": "全面协调可持续",
                "option_b": "以人为本",
                "option_c": "发展",
                "option_d": "统筹兼顾",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "2007年党的十七大报告指出，科学发展观的根本方法是？",
                "option_a": "以人为本",
                "option_b": "统筹兼顾",
                "option_c": "全面协调可持续",
                "option_d": "发展",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "2012年11月，习近平在参观《复兴之路》展览时首次提出的重要概念是？",
                "option_a": "新时代",
                "option_b": "人类命运共同体",
                "option_c": "一带一路",
                "option_d": "中国梦",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "2013年9月和10月，习近平分别提出建设‘新丝绸之路经济带’和‘21世纪海上丝绸之路’的合作倡议，简称？",
                "option_a": "海上丝绸之路",
                "option_b": "丝绸之路经济带",
                "option_c": "一带一路",
                "option_d": "丝绸之路合作倡议",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "2014年12月，习近平在江苏调研时首次提出的‘四个全面’战略布局是指全面建成小康社会、全面深化改革、全面依法治国和？",
                "option_a": "全面从严治党",
                "option_b": "全面建设社会主义现代化国家",
                "option_c": "全面推进党的建设新的伟大工程",
                "option_d": "全面推进国防和军队现代化",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "2015年10月，党的十八届五中全会提出的新发展理念是？",
                "option_a": "富强、民主、文明、和谐",
                "option_b": "改革、发展、稳定",
                "option_c": "创新、协调、绿色、开放、共享",
                "option_d": "自由、平等、公正、法治",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "2016年2月，习近平在党的新闻舆论工作座谈会上提出的新闻舆论工作的职责和使命是？",
                "option_a": "高举旗帜、引领导向，围绕中心、服务大局，团结人民、鼓舞士气，成风化人、凝心聚力，澄清谬误、明辨是非，联接中外、沟通世界",
                "option_b": "以科学的理论武装人，以正确的舆论引导人，以高尚的精神塑造人，以优秀的作品鼓舞人",
                "option_c": "坚持正确政治方向，坚持正确舆论导向，坚持正确新闻志向，坚持正确工作取向",
                "option_d": "传播正能量，弘扬主旋律",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "2017年10月，党的十九大报告指出，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾，这一判断的依据是？",
                "option_a": "我国社会生产力水平总体上显著提高，社会生产能力在很多方面进入世界前列",
                "option_b": "人民生活水平显著提高，对美好生活的向往更加强烈",
                "option_c": "影响满足人民美好生活需要的因素很多，但主要是发展的不平衡不充分问题",
                "option_d": "以上都是",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "2018年3月，第十三届全国人民代表大会第一次会议通过的宪法修正案，确立了习近平新时代中国特色社会主义思想在国家和社会生活中的指导地位，这是在第几次宪法修正案中增加的？",
                "option_a": "第四次",
                "option_b": "第五次",
                "option_c": "第三次",
                "option_d": "第二次",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "2019年5月，习近平在‘不忘初心、牢记使命’主题教育工作会议上指出，这次主题教育的总要求是？",
                "option_a": "守初心、担使命，找差距、抓落实",
                "option_b": "不忘初心、牢记使命，高举中国特色社会主义伟大旗帜，决胜全面建成小康社会，夺取新时代中国特色社会主义伟大胜利，为实现中华民族伟大复兴的中国梦不懈奋斗",
                "option_c": "坚持思想建党、理论强党，坚持学思用贯通、知信行统一",
                "option_d": "以县处级以上领导干部为重点，在全党开展",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "2020年10月，党的十九届五中全会审议通过的《中共中央关于制定国民经济和社会发展第十四个五年规划和二〇三五年远景目标的建议》指出，‘十四五’时期经济社会发展要以推动什么为主题？",
                "option_a": "协调发展",
                "option_b": "高速增长",
                "option_c": "创新发展",
                "option_d": "高质量发展",
                "correct_answer": "D",
                "difficulty": 2
            },
            {
                "question_text": "2021年7月1日，习近平在庆祝中国共产党成立100周年大会上庄严宣告，我们实现了第一个百年奋斗目标，在中华大地上全面建成了小康社会，历史性地解决了绝对贫困问题，正在意气风发向着全面建成社会主义现代化强国的第二个百年奋斗目标迈进。第二个百年奋斗目标是到哪一年？",
                "option_a": "本世纪中叶",
                "option_b": "2035年",
                "option_c": "2049年",
                "option_d": "2050年",
                "correct_answer": "A",
                "difficulty": 2
            },
            {
                "question_text": "2022年10月，党的二十大报告指出，全面建设社会主义现代化国家、全面推进中华民族伟大复兴，关键在？",
                "option_a": "人民",
                "option_b": "党",
                "option_c": "发展",
                "option_d": "创新",
                "correct_answer": "B",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党的最高理想和最终目标是实现共产主义，这是由党的什么决定的？",
                "option_a": "章程",
                "option_b": "纲领",
                "option_c": "性质",
                "option_d": "宗旨",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党的根本宗旨是全心全意为人民服务，这一宗旨是由党的什么决定的？",
                "option_a": "路线",
                "option_b": "纲领",
                "option_c": "性质",
                "option_d": "政策",
                "correct_answer": "C",
                "difficulty": 2
            },
            {
                "question_text": "中国共产党的组织原则是民主集中制，其基本原则不包括下列哪一项？",
                "option_a": "个人服从组织，少数服从多数，下级服从上级，全党服从中央",
                "option_b": "党的各级领导机关，除它们派出的代表机关和在非党组织中的党组外，都由选举产生",
                "option_c": "党的最高领导机关，是党的全国代表大会和它所产生的中央委员会",
                "option_d": "党禁止任何形式的个人崇拜",
                "correct_answer": "D",
                "difficulty": 2
            },
            {"question_text": "中国共产党在社会主义初级阶段的基本路线核心内容是什么？",
             "option_a": "改革开放", "option_b": "四项基本原则", "option_c": "一个中心，两个基本点",
             "option_d": "以经济建设为中心", "correct_answer": "C", "difficulty": 3},
            {"question_text": "马克思主义中国化的第一次历史性飞跃成果是什么？", "option_a": "邓小平理论",
             "option_b": "毛泽东思想", "option_c": "三个代表重要思想", "option_d": "科学发展观", "correct_answer": "B",
             "difficulty": 3},
            {"question_text": "中国特色社会主义最本质的特征是什么？", "option_a": "共同富裕", "option_b": "党的领导",
             "option_c": "市场经济", "option_d": "改革开放", "correct_answer": "B", "difficulty": 3},
            {"question_text": "党的十九大报告指出，从2020年到2035年，我国发展的目标是？", "option_a": "全面建成小康社会",
             "option_b": "基本实现社会主义现代化", "option_c": "建成社会主义现代化强国", "option_d": "实现共同富裕",
             "correct_answer": "B", "difficulty": 3},
            {"question_text": "中国共产党的根本宗旨是？", "option_a": "全心全意为人民服务", "option_b": "实现共产主义",
             "option_c": "解放和发展生产力", "option_d": "坚持党的领导", "correct_answer": "A", "difficulty": 3},
            {"question_text": "邓小平理论的精髓是？", "option_a": "改革开放", "option_b": "解放思想，实事求是",
             "option_c": "社会主义本质", "option_d": "三个有利于", "correct_answer": "B", "difficulty": 3},
            {"question_text": "党的思想路线的核心是？", "option_a": "求真务实", "option_b": "解放思想",
             "option_c": "与时俱进", "option_d": "实事求是", "correct_answer": "D", "difficulty": 3},
            {"question_text": "中国共产党成立的时间是？", "option_a": "1919年", "option_b": "1921年",
             "option_c": "1949年", "option_d": "1978年", "correct_answer": "B", "difficulty": 3},
            {"question_text": "新时代我国社会主要矛盾已经转化为？",
             "option_a": "人民日益增长的物质文化需要同落后的社会生产之间的矛盾",
             "option_b": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾", "option_c": "阶级矛盾",
             "option_d": "经济基础与上层建筑的矛盾", "correct_answer": "B", "difficulty": 3},
            {"question_text": "四个意识是指政治意识、大局意识、核心意识和？", "option_a": "看齐意识",
             "option_b": "服务意识", "option_c": "创新意识", "option_d": "改革意识", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "党的二十大报告指出，全面建设社会主义现代化国家的首要任务是？", "option_a": "高质量发展",
             "option_b": "共同富裕", "option_c": "科技创新", "option_d": "国家安全", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "中国共产党百年奋斗的历史意义不包括？", "option_a": "从根本上改变中国人民的前途命运",
             "option_b": "开辟了实现中华民族伟大复兴的正确道路", "option_c": "展示了马克思主义的强大生命力",
             "option_d": "实现了社会主义现代化", "correct_answer": "D", "difficulty": 3},
            {"question_text": "习近平新时代中国特色社会主义思想的核心要义是？", "option_a": "十个明确",
             "option_b": "十四个坚持", "option_c": "十三个方面成就", "option_d": "以上都是", "correct_answer": "D",
             "difficulty": 3},
            {"question_text": "中国共产党的最大政治优势是？", "option_a": "统一战线", "option_b": "实事求是",
             "option_c": "独立自主", "option_d": "密切联系群众", "correct_answer": "D", "difficulty": 3},
            {"question_text": "党的纪律中最重要、最根本、最关键的纪律是？", "option_a": "政治纪律", "option_b": "组织纪律",
             "option_c": "廉洁纪律", "option_d": "群众纪律", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国特色社会主义制度的最大优势是？", "option_a": "人民代表大会制度",
             "option_b": "中国共产党领导", "option_c": "社会主义市场经济体制", "option_d": "基层群众自治制度",
             "correct_answer": "B", "difficulty": 3},
            {"question_text": "全面深化改革的总目标是完善和发展中国特色社会主义制度，推进？",
             "option_a": "国家治理体系和治理能力现代化", "option_b": "社会主义市场经济体制改革",
             "option_c": "党的建设新的伟大工程", "option_d": "全面依法治国", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党在过渡时期的总路线的主体是？", "option_a": "实现社会主义工业化",
             "option_b": "对农业的社会主义改造", "option_c": "对手工业的社会主义改造",
             "option_d": "对资本主义工商业的社会主义改造", "correct_answer": "A", "difficulty": 3},
            {"question_text": "党的三大优良作风是理论联系实际、密切联系群众和？", "option_a": "批评与自我批评",
             "option_b": "艰苦奋斗", "option_c": "实事求是", "option_d": "与时俱进", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "习近平总书记提出的‘四个自信’不包括？", "option_a": "道路自信", "option_b": "理论自信",
             "option_c": "制度自信", "option_d": "文化自信", "correct_answer": "D", "difficulty": 3},
            {"question_text": "中国共产党第一次全国代表大会召开的地点是？", "option_a": "北京", "option_b": "上海",
             "option_c": "广州", "option_d": "武汉", "correct_answer": "B", "difficulty": 3},
            {"question_text": "‘一带一路’倡议的核心理念是？", "option_a": "共商共建共享", "option_b": "互利共赢",
             "option_c": "开放包容", "option_d": "和平发展", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党的最高理想和最终目标是？", "option_a": "实现中华民族伟大复兴",
             "option_b": "建设中国特色社会主义", "option_c": "实现共产主义", "option_d": "全面建成小康社会",
             "correct_answer": "C", "difficulty": 3},
            {"question_text": "党的十九届六中全会通过的重要文件是？",
             "option_a": "《中共中央关于党的百年奋斗重大成就和历史经验的决议》",
             "option_b": "《中共中央关于全面深化改革若干重大问题的决定》",
             "option_c": "《中共中央关于全面推进依法治国若干重大问题的决定》",
             "option_d": "《中共中央关于制定国民经济和社会发展第十四个五年规划和二〇三五年远景目标的建议》",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国特色社会主义进入新时代的历史方位是在党的哪次全国代表大会上提出的？",
             "option_a": "十七大", "option_b": "十八大", "option_c": "十九大", "option_d": "二十大",
             "correct_answer": "C", "difficulty": 3},
            {"question_text": "‘两个维护’是指坚决维护习近平总书记党中央的核心、全党的核心地位，坚决维护？",
             "option_a": "党中央权威和集中统一领导", "option_b": "党的全面领导", "option_c": "中国特色社会主义制度",
             "option_d": "党的团结统一", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党区别于其他任何政党的显著标志是？", "option_a": "独立自主",
             "option_b": "实事求是", "option_c": "三大优良作风", "option_d": "群众路线", "correct_answer": "C",
             "difficulty": 3},
            {"question_text": "全面依法治国的总目标是建设中国特色社会主义法治体系，建设？",
             "option_a": "社会主义法治国家", "option_b": "社会主义法治政府", "option_c": "社会主义法治社会",
             "option_d": "社会主义法治体系", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党在新时代的强军目标是建设一支听党指挥、能打胜仗、的人民军队？",
             "option_a": "作风优良", "option_b": "纪律严明", "option_c": "保障有力", "option_d": "英勇善战",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "‘十四五’规划的起止时间是？", "option_a": "2020-2024年", "option_b": "2021-2025年",
             "option_c": "2022-2026年", "option_d": "2023-2027年", "correct_answer": "B", "difficulty": 3},
            {"question_text": "中国共产党的性质是？",
             "option_a": "中国工人阶级的先锋队", "option_b": "中国工人阶级的先锋队，同时是中国人民和中华民族的先锋队",
             "option_c": "中国人民和中华民族的先锋队", "option_d": "无产阶级政党", "correct_answer": "B",
             "difficulty": 3},
            {"question_text": "党的思想建设的首要任务是？", "option_a": "坚定理想信念", "option_b": "加强理论武装",
             "option_c": "坚持实事求是", "option_d": "密切联系群众", "correct_answer": "A", "difficulty": 3},
            {"question_text": "‘四个伟大’中起决定性作用的是？", "option_a": "伟大斗争", "option_b": "伟大工程",
             "option_c": "伟大事业", "option_d": "伟大梦想", "correct_answer": "B", "difficulty": 3},
            {"question_text": "中国共产党的根本组织原则是？", "option_a": "民主集中制", "option_b": "集体领导制度",
             "option_c": "少数服从多数", "option_d": "下级服从上级", "correct_answer": "A", "difficulty": 3},
            {"question_text": "马克思主义的活的灵魂是？", "option_a": "具体问题具体分析", "option_b": "实事求是",
             "option_c": "辩证唯物主义", "option_d": "历史唯物主义", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党历史上的第一个中央纪律检查机构是？", "option_a": "中央纪律检查委员会",
             "option_b": "中央监察委员会", "option_c": "中央审查委员会", "option_d": "中央监察部",
             "correct_answer": "B", "difficulty": 3},
            {"question_text": "‘不忘初心、牢记使命’主题教育的总要求是守初心、担使命，找差距、？", "option_a": "抓落实",
             "option_b": "抓整改", "option_c": "抓学习", "option_d": "抓作风", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党领导人民治理国家的基本方略是？", "option_a": "依法治国", "option_b": "以德治国",
             "option_c": "依规治党", "option_d": "民主集中制", "correct_answer": "A", "difficulty": 3},
            {"question_text": "社会主义核心价值观中，国家层面的价值目标是？", "option_a": "富强、民主、文明、和谐",
             "option_b": "自由、平等、公正、法治", "option_c": "爱国、敬业、诚信、友善", "option_d": "以上都是",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党在抗日战争时期的土地政策是？", "option_a": "减租减息", "option_b": "耕者有其田",
             "option_c": "土地国有化", "option_d": "土地集体化", "correct_answer": "A", "difficulty": 3},
            {"question_text": "党的群众路线的基本内容是一切为了群众，一切依靠群众，从群众中来，？",
             "option_a": "联系群众", "option_b": "服务群众", "option_c": "到群众中去", "option_d": "相信群众",
             "correct_answer": "C", "difficulty": 3},
            {"question_text": "中国特色社会主义事业总体布局是？", "option_a": "四位一体", "option_b": "五位一体",
             "option_c": "三位一体", "option_d": "六位一体", "correct_answer": "B", "difficulty": 3},
            {"question_text": "‘一带一路’建设的主要内容是政策沟通、设施联通、贸易畅通、资金融通、？", "option_a": "民心相通",
             "option_b": "文化相通", "option_c": "科技相通", "option_d": "教育相通", "correct_answer": "A",
             "difficulty": 3},
            {
                "question_text": "中国共产党在新民主主义革命时期的总路线是无产阶级领导的，人民大众的，反对帝国主义、封建主义和？",
                "option_a": "殖民主义", "option_b": "资本主义", "option_c": "官僚资本主义", "option_d": "买办资产阶级",
                "correct_answer": "C", "difficulty": 3},
            {"question_text": "党的十九大报告指出，我国经济已由高速增长阶段转向阶段？", "option_a": "高质量发展",
             "option_b": "中高速增长", "option_c": "中速增长", "option_d": "低速增长", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "中国共产党的行动指南不包括？", "option_a": "马克思列宁主义", "option_b": "毛泽东思想",
             "option_c": "邓小平理论", "option_d": "三民主义", "correct_answer": "D", "difficulty": 3},
            {"question_text": "全面从严治党的根本遵循是？", "option_a": "党内法规", "option_b": "宪法",
             "option_c": "党章", "option_d": "党的纪律", "correct_answer": "C", "difficulty": 3},
            {
                "question_text": "中国共产党在社会主义初级阶段的基本经济制度是公有制为主体、多种所有制经济共同发展，按劳分配为主体、多种分配方式并存，？",
                "option_a": "社会主义市场经济体制", "option_b": "计划经济体制", "option_c": "混合经济体制",
                "option_d": "市场经济体制", "correct_answer": "A", "difficulty": 3},
            {"question_text": "‘两个一百年’奋斗目标中，第一个一百年的目标是？", "option_a": "建成社会主义现代化强国",
             "option_b": "基本实现社会主义现代化", "option_c": "全面建成小康社会",
             "option_d": "实现中华民族伟大复兴", "correct_answer": "C", "difficulty": 3},
            {"question_text": "中国共产党历史上具有生死攸关转折点意义的会议是？", "option_a": "遵义会议",
             "option_b": "古田会议", "option_c": "瓦窑堡会议", "option_d": "洛川会议", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "习近平总书记指出，是关系党的事业兴衰成败第一位的问题？", "option_a": "道路问题",
             "option_b": "理论问题", "option_c": "制度问题", "option_d": "作风问题", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "中国共产党的三大历史任务是推进现代化建设、完成祖国统一、？",
             "option_a": "实现中华民族伟大复兴", "option_b": "维护世界和平与促进共同发展",
             "option_c": "全面建成小康社会", "option_d": "建设社会主义现代化强国", "correct_answer": "B",
             "difficulty": 3},
            {"question_text": "党的组织建设的重点是？", "option_a": "完善党内监督体系",
             "option_b": "健全民主集中制", "option_c": "加强基层党组织建设", "option_d": "造就高素质党员、干部队伍",
             "correct_answer": "D", "difficulty": 3},
            {"question_text": "‘三严三实’中的‘三严’是指严以修身、严以用权、？", "option_a": "严以执法",
             "option_b": "严以治家", "option_c": "严以律己", "option_d": "严以待人", "correct_answer": "C",
             "difficulty": 3},
            {"question_text": "中国共产党领导的多党合作和政治协商制度的基本方针是长期共存、互相监督、肝胆相照、？",
             "option_a": "荣辱与共", "option_b": "共同发展", "option_c": "民主协商", "option_d": "参政议政",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "社会主义的本质是解放和发展生产力，消灭剥削，消除两极分化，最终达到？",
             "option_a": "共同富裕", "option_b": "共产主义", "option_c": "社会主义现代化", "option_d": "全面小康",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "党的纪律处分有警告、严重警告、撤销党内职务、留党察看、？", "option_a": "开除党籍",
             "option_b": "记过", "option_c": "记大过", "option_d": "降级", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国特色社会主义法治道路的核心要义不包括？", "option_a": "坚持党的领导",
             "option_b": "坚持中国特色社会主义制度", "option_c": "贯彻中国特色社会主义法治理论",
             "option_d": "照搬西方宪政模式", "correct_answer": "D", "difficulty": 3},
            {"question_text": "‘两学一做’学习教育的内容是学党章党规、学系列讲话，？", "option_a": "做模范党员",
             "option_b": "做优秀党员", "option_c": "做合格党员", "option_d": "做先进党员", "correct_answer": "C",
             "difficulty": 3},
            {"question_text": "中国共产党在新时代的历史使命是实现？", "option_a": "中华民族伟大复兴的中国梦",
             "option_b": "社会主义现代化", "option_c": "共同富裕", "option_d": "全面建成小康社会",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "党的政治建设的首要任务是？", "option_a": "保证全党服从中央，坚持党中央权威和集中统一领导",
             "option_b": "坚定政治信仰", "option_c": "严明政治纪律和政治规矩", "option_d": "净化党内政治生态",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党与各民主党派合作的基本方针中，‘长期共存’的前提是？", "option_a": "坚持党的领导",
             "option_b": "坚持四项基本原则", "option_c": "坚持社会主义道路", "option_d": "坚持人民民主专政",
             "correct_answer": "B", "difficulty": 3},
            {"question_text": "马克思主义中国化的最新成果是？", "option_a": "三个代表重要思想",
             "option_b": "邓小平理论", "option_c": "习近平新时代中国特色社会主义思想", "option_d": "科学发展观", "correct_answer": "C",
             "difficulty": 3},
            {"question_text": "党的思想路线的完整表述是一切从实际出发，理论联系实际，实事求是，？",
             "option_a": "解放思想", "option_b": "在实践中检验真理和发展真理", "option_c": "与时俱进",
             "option_d": "求真务实", "correct_answer": "B", "difficulty": 3},
            {"question_text": "中国共产党在社会主义初级阶段的奋斗目标是把我国建设成为富强民主文明和谐美丽的？",
             "option_a": "社会主义现代化国家", "option_b": "社会主义现代化强国", "option_c": "小康社会",
             "option_d": "共产主义社会", "correct_answer": "B", "difficulty": 3},
            {"question_text": "‘四个全面’战略布局中，居于引领地位的是？", "option_a": "全面建设社会主义现代化国家",
             "option_b": "全面深化改革", "option_c": "全面依法治国", "option_d": "全面从严治党", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "中国共产党的根本宗旨是由党的什么决定的？", "option_a": "性质", "option_b": "纲领",
             "option_c": "章程", "option_d": "路线", "correct_answer": "A", "difficulty": 3},
            {"question_text": "党的组织生活的基本制度是？", "option_a": "‘三会一课’", "option_b": "民主生活会",
             "option_c": "组织生活会", "option_d": "民主评议党员", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党在长期奋斗中形成的精神谱系的核心是？", "option_a": "伟大建党精神",
             "option_b": "井冈山精神", "option_c": "长征精神", "option_d": "延安精神", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "全面深化改革的重点是？", "option_a": "社会体制改革", "option_b": "政治体制改革",
             "option_c": "文化体制改革", "option_d": "经济体制改革", "correct_answer": "D", "difficulty": 3},
            {"question_text": "中国共产党的最高领导机关是？", "option_a": "中央政治局",
             "option_b": "党的全国代表大会和中央委员会", "option_c": "中央政治局常务委员会", "option_d": "中央委员会总书记",
             "correct_answer": "B", "difficulty": 3},
            {"question_text": "‘五位一体’总体布局中，生态文明建设的核心是？", "option_a": "坚持人与自然和谐共生",
             "option_b": "绿色发展", "option_c": "节约资源和保护环境", "option_d": "建设美丽中国",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党的群众路线教育实践活动的主要任务是集中解决形式主义、官僚主义、享乐主义和？",
             "option_a": "奢靡之风", "option_b": "宗派主义", "option_c": "主观主义", "option_d": "经验主义",
             "correct_answer": "A", "difficulty": 3},
            {"question_text": "社会主义初级阶段的基本国情是我国最大的实际，这个阶段至少需要多少年？", "option_a": "200年",
             "option_b": "50年", "option_c": "100年", "option_d": "150年", "correct_answer": "C", "difficulty": 3},
            {"question_text": "中国共产党的纪律检查机关的主要职责是监督、执纪、？", "option_a": "问责", "option_b": "审查",
             "option_c": "调查", "option_d": "处分", "correct_answer": "A", "difficulty": 3},
            {"question_text": "‘一带一路’倡议提出的时间是？", "option_a": "2013年", "option_b": "2014年",
             "option_c": "2015年", "option_d": "2016年", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党的入党誓词中，‘为共产主义奋斗终身，随时准备为党和人民牺牲一切，？’",
             "option_a": "永不叛党", "option_b": "永不褪色", "option_c": "永不松懈", "option_d": "永不变质",
             "correct_answer": "A", "difficulty": 3},
            {
                "question_text": "党的十九大报告指出，我国社会主要矛盾的变化，没有改变我们对我国社会主义所处历史阶段的判断，我国仍处于并将长期处于？",
                "option_a": "社会主义初级阶段", "option_b": "社会主义中级阶段", "option_c": "社会主义高级阶段",
                "option_d": "共产主义初级阶段", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党的组织原则民主集中制的基本原则中，‘四个服从’的核心是？",
             "option_a": "全党服从中央", "option_b": "少数服从多数", "option_c": "下级服从上级",
             "option_d": "个人服从组织", "correct_answer": "A", "difficulty": 3},
            {"question_text": "习近平总书记强调，是共产党人精神上的‘钙’？", "option_a": "理想信念",
             "option_b": "党性修养", "option_c": "宗旨意识", "option_d": "纪律观念", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "中国特色社会主义法治体系的核心是？", "option_a": "宪法", "option_b": "法律",
             "option_c": "行政法规", "option_d": "党内法规", "correct_answer": "A", "difficulty": 3},
            {
                "question_text": "党的建设的五项基本要求是坚持党的基本路线，坚持解放思想、实事求是、与时俱进、求真务实，坚持全心全意为人民服务，坚持民主集中制，？",
                "option_a": "坚持从严管党治党", "option_b": "坚持党的领导", "option_c": "坚持社会主义道路",
                "option_d": "坚持马克思主义指导地位", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党在改革开放新时期的三大历史任务是推进现代化建设、完成祖国统一、？",
             "option_a": "维护世界和平与促进共同发展", "option_b": "实现中华民族伟大复兴",
             "option_c": "全面建设小康社会", "option_d": "建设社会主义现代化强国", "correct_answer": "A",
             "difficulty": 3},
            {"question_text": "‘人类命运共同体’理念首次提出的时间是？", "option_a": "2013年", "option_b": "2014年",
             "option_c": "2015年", "option_d": "2016年", "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党的历史上，首次提出‘马克思主义中国化’命题的会议是？", "option_a": "七届二中全会",
             "option_b": "七大", "option_c": "六届六中全会", "option_d": "十一届三中全会", "correct_answer": "C",
             "difficulty": 3},
            {
                "question_text": "党的二十大报告指出，全面建设社会主义现代化国家，必须坚持中国特色社会主义文化发展道路，增强文化自信，围绕举旗帜、聚民心、育新人、兴文化、？",
                "option_a": "展形象", "option_b": "促发展", "option_c": "强根基", "option_d": "谋复兴",
                "correct_answer": "A", "difficulty": 3},
            {"question_text": "中国共产党的根本工作路线是？", "option_a": "独立自主", "option_b": "实事求是",
             "option_c": "群众路线", "option_d": "统一战线", "correct_answer": "C", "difficulty": 3},
            {
                "question_text": "‘四个全面’战略布局中，全面深化改革的总目标是完善和发展中国特色社会主义制度，推进国家治理体系和治理能力？",
                "option_a": "科学化", "option_b": "法治化", "option_c": "规范化", "option_d": "现代化",
                "correct_answer": "D", "difficulty": 3},
            {"question_text": "中国共产党的纪律中，最根本的纪律是？", "option_a": "组织纪律", "option_b": "政治纪律",
             "option_c": "廉洁纪律", "option_d": "群众纪律", "correct_answer": "B", "difficulty": 3},
            {"question_text": "习近平新时代中国特色社会主义思想的核心内容是‘十个明确’、‘十四个坚持’和？",
             "option_a": "八个明确", "option_b": "十三个方面成就", "option_c": "十一个坚持", "option_d": "九个方面成就",
             "correct_answer": "B", "difficulty": 3},
            {"question_text": "中国共产党的最高理想和最终目标是实现？", "option_a": "共同富裕", "option_b": "社会主义",
             "option_c": "共产主义", "option_d": "中华民族伟大复兴", "correct_answer": "C", "difficulty": 3},
            {"question_text": "党的组织建设的基础是？", "option_a": "基层党组织建设", "option_b": "干部队伍建设",
             "option_c": "党员队伍建设", "option_d": "民主集中制建设", "correct_answer": "A", "difficulty": 3},
            {
                "question_text": "中国特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和之间的矛盾？",
                "option_a": "城乡发展差距", "option_b": "落后的社会生产", "option_c": "不平衡不充分的发展",
                "option_d": "贫富差距", "correct_answer": "C", "difficulty": 3},
            {"question_text": "中国共产党的三大法宝是统一战线、武装斗争、？", "option_a": "党的建设",
             "option_b": "群众路线", "option_c": "实事求是", "option_d": "独立自主", "correct_answer": "A",
             "difficulty": 3},
            {
                "question_text": "党的十九大报告指出，从全面建成小康社会到基本实现现代化，再到全面建成，是新时代中国特色社会主义发展的战略安排？",
                "option_a": "社会主义现代化国家", "option_b": "社会主义现代化强国", "option_c": "共产主义社会",
                "option_d": "和谐社会", "correct_answer": "B", "difficulty": 3},

        {"question_text": "中国共产党成立于哪一年？", "option_a": "1919年", "option_b": "1921年", "option_c": "1949年",
         "option_d": "1978年", "correct_answer": "B", "difficulty": 1},
        {"question_text": "中华人民共和国成立的日期是？", "option_a": "1945年8月15日", "option_b": "1945年9月2日",
         "option_c": "1949年10月1日", "option_d": "1949年10月2日", "correct_answer": "C", "difficulty": 1},
        {"question_text": "中国共产党第一次全国代表大会召开地点是？", "option_a": "北京", "option_b": "上海",
         "option_c": "广州", "option_d": "武汉", "correct_answer": "B", "difficulty": 1},
        {"question_text": "红军长征开始于哪一年？", "option_a": "1931年", "option_b": "1934年", "option_c": "1935年",
         "option_d": "1936年", "correct_answer": "B", "difficulty": 1},
        {"question_text": "抗日战争胜利的年份是？", "option_a": "1945年", "option_b": "1946年", "option_c": "1949年",
         "option_d": "1950年", "correct_answer": "A", "difficulty": 1},
        {"question_text": "‘五四运动’爆发于哪一年？", "option_a": "1911年", "option_b": "1919年", "option_c": "1921年",
         "option_d": "1927年", "correct_answer": "B", "difficulty": 1},
        {"question_text": "中国共产党的宗旨是？", "option_a": "全心全意为人民服务", "option_b": "实现共产主义",
         "option_c": "建设社会主义", "option_d": "改革开放", "correct_answer": "A", "difficulty": 1},
        {"question_text": "‘八一南昌起义’发生在哪一年？", "option_a": "1921年", "option_b": "1927年",
         "option_c": "1935年", "option_d": "1945年", "correct_answer": "B", "difficulty": 1},
        {"question_text": "毛泽东思想被确立为党的指导思想是在哪个会议？", "option_a": "中共一大", "option_b": "遵义会议",
         "option_c": "中共七大", "option_d": "中共十一届三中全会", "correct_answer": "C", "difficulty": 1},
        {"question_text": "‘改革开放’政策开始于哪一年？", "option_a": "1949年", "option_b": "1966年",
         "option_c": "1978年", "option_d": "1992年", "correct_answer": "C", "difficulty": 1},
        {"question_text": "中国共产党的最高理想和最终目标是？", "option_a": "共同富裕", "option_b": "社会主义现代化",
         "option_c": "实现共产主义", "option_d": "全面小康", "correct_answer": "C", "difficulty": 1},
        {"question_text": "‘三个代表’重要思想的提出者是？", "option_a": "毛泽东", "option_b": "邓小平",
         "option_c": "江泽民", "option_d": "胡锦涛", "correct_answer": "C", "difficulty": 1},
        {"question_text": "科学发展观的核心是？", "option_a": "发展", "option_b": "以人为本",
         "option_c": "全面协调可持续", "option_d": "统筹兼顾", "correct_answer": "B", "difficulty": 1},
        {"question_text": "习近平新时代中国特色社会主义思想确立于党的哪次全国代表大会？", "option_a": "十七大",
         "option_b": "十八大", "option_c": "十九大", "option_d": "二十大", "correct_answer": "C", "difficulty": 1},
        {"question_text": "‘一带一路’倡议提出于哪一年？", "option_a": "2012年", "option_b": "2013年",
         "option_c": "2014年", "option_d": "2015年", "correct_answer": "B", "difficulty": 1},
        {"question_text": "中国共产党党员必须履行的义务不包括？", "option_a": "认真学习", "option_b": "缴纳党费",
         "option_c": "个人致富", "option_d": "对党忠诚", "correct_answer": "C", "difficulty": 1},
        {"question_text": "‘两个一百年’奋斗目标中第一个百年目标是？", "option_a": "全面建成小康社会",
         "option_b": "基本实现现代化", "option_c": "建成社会主义现代化强国", "option_d": "实现共同富裕",
         "correct_answer": "A", "difficulty": 1},
        {"question_text": "中国共产党的根本组织原则是？", "option_a": "民主集中制", "option_b": "少数服从多数",
         "option_c": "下级服从上级", "option_d": "集体领导", "correct_answer": "A", "difficulty": 1},
        {"question_text": "‘不忘初心、牢记使命’中的‘初心’是指？", "option_a": "为中国人民谋幸福",
         "option_b": "为中华民族谋复兴", "option_c": "全心全意为人民服务", "option_d": "实现共产主义",
         "correct_answer": "A", "difficulty": 1},
        {"question_text": "中国特色社会主义进入新时代是在党的哪次会议上提出的？", "option_a": "十七大",
         "option_b": "十八大", "option_c": "十九大", "option_d": "二十大", "correct_answer": "C", "difficulty": 1},
        {"question_text": "‘四个意识’不包括以下哪项？", "option_a": "政治意识", "option_b": "大局意识",
         "option_c": "核心意识", "option_d": "创新意识", "correct_answer": "D", "difficulty": 1},
        {"question_text": "中国共产党的象征和标志是？", "option_a": "党旗", "option_b": "党徽党旗", "option_c": "党徽",
         "option_d": "国旗", "correct_answer": "B", "difficulty": 1},
        {"question_text": "‘五位一体’总体布局不包括以下哪个方面？", "option_a": "经济建设", "option_b": "政治建设",
         "option_c": "文化建设", "option_d": "军事建设", "correct_answer": "D", "difficulty": 1},
        {"question_text": "‘四个全面’战略布局中居于引领地位的是？", "option_a": "全面建设社会主义现代化国家",
         "option_b": "全面深化改革", "option_c": "全面依法治国", "option_d": "全面从严治党", "correct_answer": "A",
         "difficulty": 1},
        {"question_text": "中国共产党历史上的‘三大战役’不包括？", "option_a": "辽沈战役", "option_b": "淮海战役",
         "option_c": "平津战役", "option_d": "渡江战役", "correct_answer": "D", "difficulty": 1},
        {"question_text": "‘两学一做’学习教育指的是学党章党规、学系列讲话，做？", "option_a": "合格党员",
         "option_b": "优秀党员", "option_c": "模范党员", "option_d": "先进党员", "correct_answer": "A",
         "difficulty": 1},
        {"question_text": "中国共产党的最高领导机关是？", "option_a": "中央政治局", "option_b": "中央委员会",
         "option_c": "党的全国代表大会和中央委员会", "option_d": "中央政治局常务委员会", "correct_answer": "C",
         "difficulty": 1},
        {"question_text": "‘三严三实’中的‘三实’不包括？", "option_a": "谋事要实", "option_b": "创业要实",
         "option_c": "做人要实", "option_d": "工作要实", "correct_answer": "D", "difficulty": 1},
        {"question_text": "中国共产党成立的标志是？", "option_a": "五四运动爆发", "option_b": "中共一大召开",
         "option_c": "南昌起义", "option_d": "秋收起义", "correct_answer": "B", "difficulty": 1},
        {"question_text": "‘红船精神’的核心是？", "option_a": "开天辟地、敢为人先", "option_b": "坚定理想、百折不挠",
         "option_c": "立党为公、忠诚为民", "option_d": "以上都是", "correct_answer": "D", "difficulty": 1},

        {"question_text": "遵义会议召开的主要历史意义是？", "option_a": "决定北上抗日",
         "option_b": "决定开展土地革命", "option_c": "确立了毛泽东在党中央和红军的领导地位", "option_d": "宣告长征胜利结束",
         "correct_answer": "C", "difficulty": 2},
        {"question_text": "抗日战争时期，中国共产党领导的八路军取得的第一次大捷是？", "option_a": "平型关大捷",
         "option_b": "台儿庄战役", "option_c": "百团大战", "option_d": "淞沪会战", "correct_answer": "A",
         "difficulty": 2},
        {"question_text": "‘农村包围城市，武装夺取政权’革命道路的理论最早提出于？", "option_a": "南昌起义后",
         "option_b": "秋收起义后", "option_c": "遵义会议后", "option_d": "抗日战争时期", "correct_answer": "B",
         "difficulty": 2},
        {"question_text": "中共十一届三中全会作出的历史性决策是？", "option_a": "建立社会主义市场经济体制",
         "option_b": "实行改革开放", "option_c": "提出社会主义初级阶段理论",
         "option_d": "确立邓小平理论为党的指导思想", "correct_answer": "B", "difficulty": 2},
        {"question_text": "‘一国两制’构想最初是为解决哪个问题提出的？", "option_a": "香港问题", "option_b": "澳门问题",
         "option_c": "台湾问题", "option_d": "西藏问题", "correct_answer": "C", "difficulty": 2},
        {"question_text": "中国共产党在过渡时期总路线的主体是？", "option_a": "对手工业的社会主义改造",
         "option_b": "对农业的社会主义改造", "option_c": "实现社会主义工业化",
         "option_d": "对资本主义工商业的社会主义改造", "correct_answer": "C", "difficulty": 2},
        {"question_text": "‘文化大革命’结束的标志是？", "option_a": "粉碎‘四人帮’", "option_b": "十一届三中全会召开",
         "option_c": "邓小平复出", "option_d": "真理标准问题大讨论", "correct_answer": "A", "difficulty": 2},
        {"question_text": "毛泽东《论持久战》发表于哪一年？", "option_a": "1931年", "option_b": "1937年",
         "option_c": "1938年", "option_d": "1945年", "correct_answer": "C", "difficulty": 2},
        {"question_text": "中国共产党在新民主主义革命时期的三大法宝是？", "option_a": "实事求是、群众路线、独立自主",
         "option_b": "土地革命、武装斗争、根据地建设", "option_c": "统一战线、武装斗争、党的建设",
         "option_d": "理论联系实际、密切联系群众、批评与自我批评", "correct_answer": "C", "difficulty": 2},
        {"question_text": "‘改革开放’的起点是？", "option_a": "中共十一届三中全会", "option_b": "中共十二大",
         "option_c": "南方谈话", "option_d": "中共十四大", "correct_answer": "A", "difficulty": 2},
        {"question_text": "社会主义初级阶段理论首次提出于党的哪次会议？", "option_a": "十一届三中全会",
         "option_b": "十二大", "option_c": "十三大", "option_d": "十四大", "correct_answer": "C", "difficulty": 2},
        {"question_text": "‘三个有利于’标准的提出者是？", "option_a": "毛泽东", "option_b": "邓小平",
         "option_c": "江泽民", "option_d": "胡锦涛", "correct_answer": "B", "difficulty": 2},
        {"question_text": "中国加入世界贸易组织（WTO）的时间是？", "option_a": "1997年", "option_b": "2001年",
         "option_c": "2008年", "option_d": "2012年", "correct_answer": "B", "difficulty": 2},
        {"question_text": "‘中国梦’的核心目标可以概括为‘两个一百年’的目标，具体是指？",
         "option_a": "到建党100年时全面深化改革，到新中国成立100年时全面依法治国",
         "option_b": "到建党100年时基本实现现代化，到新中国成立100年时建成共产主义社会",
         "option_c": "到建党100年时实现共同富裕，到新中国成立100年时实现社会主义现代化",
         "option_d": "到建党100年时全面建成小康社会，到新中国成立100年时建成富强民主文明和谐的社会主义现代化国家", "correct_answer": "D",
         "difficulty": 2},
        {"question_text": "中国共产党历史上的‘延安整风运动’主要解决的问题是？", "option_a": "主观主义、宗派主义、党八股",
         "option_b": "官僚主义、形式主义、享乐主义", "option_c": "教条主义、经验主义、主观主义",
         "option_d": "个人主义、拜金主义、享乐主义", "correct_answer": "A", "difficulty": 2},
        {"question_text": "‘和平共处五项原则’首次提出于哪一年？", "option_a": "1953年", "option_b": "1955年",
         "option_c": "1971年", "option_d": "1978年", "correct_answer": "A", "difficulty": 2},
        {"question_text": "中国共产党在社会主义初级阶段的基本路线的核心内容是？", "option_a": "一个中心，两个基本点",
         "option_b": "四项基本原则", "option_c": "改革开放", "option_d": "以经济建设为中心", "correct_answer": "A",
         "difficulty": 2},
        {"question_text": "‘两弹一星’中的‘两弹’指的是？", "option_a": "原子弹、氢弹", "option_b": "原子弹、导弹",
         "option_c": "氢弹、导弹", "option_d": "原子弹、人造卫星", "correct_answer": "B", "difficulty": 2},
        {"question_text": "中共十九大报告指出，我国社会主要矛盾已经转化为？",
         "option_a": "生产力与生产关系之间的矛盾",
         "option_b": "人民日益增长的物质文化需要同落后的社会生产之间的矛盾", "option_c": "人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾",
         "option_d": "经济基础与上层建筑之间的矛盾", "correct_answer": "C", "difficulty": 2},
        {"question_text": "‘社会主义核心价值观’中，国家层面的价值目标是？", "option_a": "自由、平等、公正、法治",
         "option_b": "富强、民主、文明、和谐", "option_c": "爱国、敬业、诚信、友善", "option_d": "以上都是",
         "correct_answer": "B", "difficulty": 2},
        {"question_text": "中国共产党领导的多党合作和政治协商制度的基本方针是？",
         "option_a": "长期共存、互相监督、肝胆相照、荣辱与共", "option_b": "长期共存、互相监督、民主协商、共同发展",
         "option_c": "政治协商、民主监督、参政议政、合作共事",
         "option_d": "坚持党的领导、坚持人民民主专政、坚持社会主义道路、坚持马克思列宁主义毛泽东思想",
         "correct_answer": "A", "difficulty": 2},
        {"question_text": "‘五四运动’的直接导火索是？", "option_a": "马克思主义在中国的传播",
         "option_b": "新文化运动的兴起", "option_c": "俄国十月革命的影响", "option_d": "巴黎和会上中国外交的失败",
         "correct_answer": "D", "difficulty": 2},
        {"question_text": "中国共产党在抗日战争时期实行的土地政策是？", "option_a": "耕者有其田", "option_b": "减租减息",
         "option_c": "土地国有化", "option_d": "土地集体化", "correct_answer": "B", "difficulty": 2},
        {"question_text": "‘三大改造’的完成标志着？", "option_a": "改革开放的开始",
         "option_b": "新民主主义革命的胜利", "option_c": "社会主义制度在我国基本建立", "option_d": "社会主义现代化建设新时期的开始",
         "correct_answer": "C", "difficulty": 2},
        {"question_text": "邓小平南方谈话发表于哪一年？", "option_a": "1978年", "option_b": "1992年",
         "option_c": "1997年", "option_d": "2001年", "correct_answer": "B", "difficulty": 2},
        {"question_text": "中国共产党的‘三大优良作风’是？", "option_a": "理论联系实际、密切联系群众、批评与自我批评",
         "option_b": "实事求是、群众路线、独立自主", "option_c": "谦虚谨慎、不骄不躁、艰苦奋斗",
         "option_d": "解放思想、实事求是、与时俱进", "correct_answer": "A", "difficulty": 2},
        {"question_text": "‘一带一路’倡议的核心理念是？", "option_a": "开放包容", "option_b": "互利共赢",
         "option_c": "共商共建共享", "option_d": "和平发展", "correct_answer": "C", "difficulty": 2},
        {"question_text": "中国共产党在新民主主义革命时期的总路线是？",
         "option_a": "统一战线、武装斗争、党的建设",
         "option_b": "农村包围城市，武装夺取政权", "option_c": "无产阶级领导的，人民大众的，反对帝国主义、封建主义和官僚资本主义的革命",
         "option_d": "土地革命、武装斗争、根据地建设", "correct_answer": "C", "difficulty": 2},
        {"question_text": "‘人类命运共同体’理念首次提出于哪一年？", "option_a": "2012年", "option_b": "2013年",
         "option_c": "2015年", "option_d": "2017年", "correct_answer": "B", "difficulty": 2},
        {"question_text": "中国共产党历史上具有生死攸关转折点意义的会议是？", "option_a": "洛川会议",
         "option_b": "古田会议", "option_c": "瓦窑堡会议", "option_d": "遵义会议", "correct_answer": "D",
         "difficulty": 2},

        {"question_text": "毛泽东在《新民主主义论》中提出的新民主主义革命的政治纲领是？",
         "option_a": "建立无产阶级领导的，以工农联盟为基础的，几个革命阶级联合专政的新民主主义共和国",
         "option_b": "推翻帝国主义和封建主义的统治", "option_c": "实现社会主义工业化", "option_d": "建立社会主义制度",
         "correct_answer": "A", "difficulty": 3},
        {"question_text": "邓小平理论的精髓是？", "option_a": "解放思想，实事求是", "option_b": "改革开放",
         "option_c": "社会主义本质", "option_d": "三个有利于", "correct_answer": "A", "difficulty": 3},
        {"question_text": "中国共产党在过渡时期总路线的‘一化三改’中，‘三改’不包括以下哪项？",
         "option_a": "对农业的社会主义改造", "option_b": "对手工业的社会主义改造",
         "option_c": "对资本主义工商业的社会主义改造", "option_d": "对服务业的社会主义改造", "correct_answer": "D",
         "difficulty": 3},
        {"question_text": "‘延安精神’的核心内容不包括？", "option_a": "全心全意为人民服务的根本宗旨",
         "option_b": "解放思想、实事求是的思想路线", "option_c": "坚定正确的政治方向",
         "option_d": "自力更生、艰苦创业的奋斗精神", "correct_answer": "D", "difficulty": 3},
        {"question_text": "中共八大关于国内主要矛盾的论断是？",
         "option_a": "无产阶级和资产阶级之间的矛盾",
         "option_b": "人民对于建立先进的工业国的要求同落后的农业国的现实之间的矛盾，人民对于经济文化迅速发展的需要同当前经济文化不能满足人民需要的状况之间的矛盾", "option_c": "社会主义道路和资本主义道路之间的矛盾",
         "option_d": "人民日益增长的物质文化需要同落后的社会生产之间的矛盾", "correct_answer": "B", "difficulty": 3},
        {"question_text": "‘文化大革命’的教训不包括？", "option_a": "必须坚持党的领导",
         "option_b": "必须坚持社会主义民主和法制", "option_c": "必须以经济建设为中心",
         "option_d": "必须坚持阶级斗争为纲", "correct_answer": "D", "difficulty": 3},
        {"question_text": "毛泽东思想活的灵魂是？", "option_a": "实事求是、群众路线、独立自主",
         "option_b": "理论联系实际、密切联系群众、批评与自我批评", "option_c": "统一战线、武装斗争、党的建设",
         "option_d": "解放思想、实事求是、与时俱进", "correct_answer": "A", "difficulty": 3},
        {"question_text": "‘社会主义本质论’是邓小平在哪个场合提出的？", "option_a": "中共十三大", "option_b": "南方谈话",
         "option_c": "中共十四大", "option_d": "中共十五大", "correct_answer": "B", "difficulty": 3},
        {"question_text": "中国共产党在新时代的强军目标是建设一支什么样的人民军队？",
         "option_a": "政治合格、军事过硬、作风优良、纪律严明、保障有力", "option_b": "听党指挥、能打胜仗、作风优良",
         "option_c": "革命化、现代化、正规化", "option_d": "忠诚于党、热爱人民、报效国家、献身使命、崇尚荣誉",
         "correct_answer": "B", "difficulty": 3},
        {"question_text": "‘四个全面’战略布局中，全面深化改革的总目标是？",
         "option_a": "完善和发展中国特色社会主义制度，推进国家治理体系和治理能力现代化",
         "option_b": "实现社会主义现代化和中华民族伟大复兴", "option_c": "全面建成小康社会",
         "option_d": "建设中国特色社会主义法治体系，建设社会主义法治国家", "correct_answer": "A", "difficulty": 3},
        {"question_text": "习近平新时代中国特色社会主义思想的核心要义是？",
         "option_a": "十个明确、十四个坚持、十三个方面成就", "option_b": "解放思想、实事求是、与时俱进、求真务实",
         "option_c": "为中国人民谋幸福，为中华民族谋复兴", "option_d": "坚持和发展中国特色社会主义",
         "correct_answer": "A", "difficulty": 3},
        {"question_text": "中国共产党百年奋斗的历史意义不包括？", "option_a": "从根本上改变中国人民的前途命运",
         "option_b": "开辟了实现中华民族伟大复兴的正确道路", "option_c": "展示了马克思主义的强大生命力",
         "option_d": "实现了社会主义现代化", "correct_answer": "D", "difficulty": 3},
        {"question_text": "‘一国两制’的基本内容不包括？", "option_a": "一个中国", "option_b": "两制并存",
         "option_c": "高度自治", "option_d": "和平统一", "correct_answer": "D", "difficulty": 3},
        {"question_text": "中国共产党的政治建设的首要任务是？",
         "option_a": "保证全党服从中央，坚持党中央权威和集中统一领导", "option_b": "坚定政治信仰",
         "option_c": "严明政治纪律和政治规矩", "option_d": "净化党内政治生态", "correct_answer": "A", "difficulty": 3},
        {"question_text": "马克思主义中国化的第一次历史性飞跃成果是？", "option_a": "习近平新时代中国特色社会主义思想",
         "option_b": "邓小平理论", "option_c": "三个代表重要思想", "option_d": "毛泽东思想",
         "correct_answer": "D", "difficulty": 3},
        {"question_text": "中国特色社会主义最本质的特征是？", "option_a": "社会主义市场经济体制", "option_b": "共同富裕",
         "option_c": "中国共产党领导", "option_d": "人民当家作主", "correct_answer": "C", "difficulty": 3},
        {"question_text": "‘新发展理念’的内容是？", "option_a": "改革、发展、稳定", "option_b": "创新、协调、绿色、开放、共享",
         "option_c": "富强、民主、文明、和谐", "option_d": "自由、平等、公正、法治", "correct_answer": "B", "difficulty": 3},
        {"question_text": "中国共产党在社会主义初级阶段的基本经济制度是？",
         "option_a": "公有制为主体、多种所有制经济共同发展，按劳分配为主体、多种分配方式并存，社会主义市场经济体制",
         "option_b": "公有制为主体、多种所有制经济共同发展", "option_c": "按劳分配为主体、多种分配方式并存",
         "option_d": "社会主义市场经济体制", "correct_answer": "A", "difficulty": 3},
        {"question_text": "‘人类命运共同体’理念的核心内涵不包括？", "option_a": "持久和平", "option_b": "普遍安全",
         "option_c": "共同繁荣", "option_d": "单边主导", "correct_answer": "D", "difficulty": 3},
        {"question_text": "中国共产党的纪律中，最重要、最根本、最关键的纪律是？", "option_a": "群众纪律",
         "option_b": "组织纪律", "option_c": "廉洁纪律", "option_d": "政治纪律", "correct_answer": "D",
         "difficulty": 3},
        {"question_text": "‘不忘初心、牢记使命’主题教育的总要求是？", "option_a": "守初心、担使命，找差距、抓落实",
         "option_b": "理论学习有收获、思想政治受洗礼、干事创业敢担当、为民服务解难题、清正廉洁作表率",
         "option_c": "学思想、强党性、重实践、建新功", "option_d": "以上都是", "correct_answer": "A", "difficulty": 3},
        {"question_text": "中国共产党在新时代的历史使命是？", "option_a": "实现中华民族伟大复兴的中国梦",
         "option_b": "全面建设社会主义现代化国家", "option_c": "全面深化改革", "option_d": "全面从严治党",
         "correct_answer": "A", "difficulty": 3},
        {"question_text": "‘四个自信’的内容是？", "option_a": "道路自信、理论自信、制度自信、文化自信",
         "option_b": "道路自信、理论自信、制度自信、发展自信", "option_c": "道路自信、理论自信、文化自信、改革自信",
         "option_d": "道路自信、制度自信、文化自信、创新自信", "correct_answer": "A", "difficulty": 3},
        {"question_text": "中国共产党的最大政治优势是？", "option_a": "实事求是", "option_b": "密切联系群众",
         "option_c": "独立自主", "option_d": "统一战线", "correct_answer": "A", "difficulty": 3},
        {"question_text": "全面依法治国的总目标是？", "option_a": "推进科学立法、严格执法、公正司法、全民守法",
         "option_b": "完善中国特色社会主义法律体系", "option_c": "建设中国特色社会主义法治体系，建设社会主义法治国家",
         "option_d": "坚持党的领导、人民当家作主、依法治国有机统一", "correct_answer": "C", "difficulty": 3},
        {"question_text": "‘两个维护’的具体内容是？",
         "option_a": "坚决维护习近平总书记党中央的核心、全党的核心地位，坚决维护党中央权威和集中统一领导",
         "option_b": "坚决维护党的领导，坚决维护社会主义制度",
         "option_c": "坚决维护国家主权、安全、发展利益，坚决维护民族团结",
         "option_d": "坚决维护改革开放，坚决维护党的基本路线", "correct_answer": "A", "difficulty": 3},
        {"question_text": "中国共产党历史上首次提出‘马克思主义中国化’命题的会议是？", "option_a": "十一届三中全会",
         "option_b": "七大", "option_c": "七届二中全会", "option_d": "六届六中全会", "correct_answer": "D",
         "difficulty": 3},
        {"question_text": "‘伟大建党精神’的内涵是？",
         "option_a": "坚持真理、坚守理想，践行初心、担当使命，不怕牺牲、英勇斗争，对党忠诚、不负人民",
         "option_b": "开天辟地、敢为人先，坚定理想、百折不挠，立党为公、忠诚为民",
         "option_c": "坚定正确的政治方向，解放思想、实事求是的思想路线，全心全意为人民服务的根本宗旨，自力更生、艰苦创业的奋斗精神",
         "option_d": "实事求是、群众路线、独立自主", "correct_answer": "A", "difficulty": 3},
        {"question_text": "中国共产党在长期奋斗中形成的精神谱系的核心是？", "option_a": "长征精神",
         "option_b": "井冈山精神", "option_c": "伟大建党精神", "option_d": "延安精神", "correct_answer": "C",
         "difficulty": 3},
        {"question_text": "党的二十大报告指出，全面建设社会主义现代化国家的首要任务是？", "option_a": "共同富裕",
         "option_b": "高质量发展", "option_c": "科技创新", "option_d": "国家安全", "correct_answer": "B", "difficulty": 3}

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
