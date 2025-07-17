# 红色文化知识问答系统

## 项目简介
这是一个基于Flask的红色文化知识问答系统，包含AI问答功能、题库练习、答题记录等功能，旨在传播红色文化知识。

## 功能特点
- 用户注册登录系统
- 红色文化知识题库练习
- 答题记录和错题本
- 用户排行榜
- AI智能问答助手(基于DeepSeek API)
- 用户头像上传和管理

## 安装运行

### 环境要求
- Python 3.7+
- 安装依赖: `pip install -r requirements.txt`

### 运行步骤
1. 设置环境变量(Windows):
   ```cmd
   set FLASK_APP=app.py
   set FLASK_ENV=development
   set DEEPSEEK_API_KEY=your_api_key_here
   ```

2. 启动应用:
   ```cmd
   flask run
   ```

3. 访问 http://localhost:5000

## 配置说明
- `DEEPSEEK_API_KEY`: DeepSeek API密钥，用于AI问答功能
- `FLASK_SECRET_KEY`: Flask会话加密密钥(生产环境必须设置)

## API使用
### AI问答接口
POST `/api/chat`
请求参数:
```json
{
  "question": "你的问题"
}
```
响应:
```json
{
  "answer": "AI回答内容"
}
```

## 项目结构
```
hongxinshuyi/
├── app.py                # 主应用文件
├── database.py           # 数据库操作
├── init_questions.py     # 初始化题库
├── requirements.txt      # 依赖列表
├── static/               # 静态资源
│   ├── css/              # 样式表
│   ├── image/            # 图片资源
│   └── js/               # JavaScript文件
└── templates/            # 模板文件
    ├── events/           # 红色人物专题
    └── *.html            # 各页面模板
```

## 注意事项
1. 生产环境请务必设置`FLASK_SECRET_KEY`
2. AI问答功能需要有效的DeepSeek API密钥
3. 默认使用SQLite数据库，数据存储在database.db文件中
