from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['message_board']
collection = db['messages']

@app.route('/', methods=['GET'])
def index():
    return "欢迎使用留言墙微信小程序！"

@app.route('/get_messages', methods=['GET'])
def get_messages():
    messages = []
    for message in collection.find():
        messages.append({'name': message['name'], 'content': message['content']})
    return jsonify({'messages': messages})

@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.get_json()
    name = data.get('name')
    content = data.get('content')
    collection.insert_one({'name': name, 'content': content})
    return "留言成功！"

# 以上代码使用了 MongoDB 数据库来存储留言信息
# 如果没有安装 MongoDB，可以先安装并启动 MongoDB 数据库
# 然后将代码中的连接字符串 'mongodb://localhost:27017/' 修改为您的 MongoDB 数据库连接字符串即可。

# 使用该留言墙微信小程序
# 用户可以通过访问 /get_messages 接口获取所有留言信息
# 并通过访问 /add_message 接口添加留言信息
# 在前端界面中，您可以使用小程序的页面、组件和样式来展示留言信息和添加留言功能。
