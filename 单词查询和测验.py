from flask import Flask, request
from PyDictionary import PyDictionary
import random

app = Flask(__name__)
dictionary = PyDictionary()

@app.route('/', methods=['GET'])
def index():
    return "欢迎使用英语单词查询微信小程序！"

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    word = data.get('word')
    meaning = dictionary.meaning(word)
    if meaning is None:
        result = "没有找到该单词的含义，请重新输入"
    else:
        result = "【%s】的含义：" % word
        for part_of_speech, definitions in meaning.items():
            result += "\n%s:" % part_of_speech.capitalize()
            for i, definition in enumerate(definitions, start=1):
                result += "\n%d. %s" % (i, definition)
    return result

@app.route('/test', methods=['GET'])
def test():
    words = list(dictionary.words())
    test_words = random.sample(words, 5)
    return "请拼写以下单词：\n%s" % "\n".join(test_words)

@app.route('/score', methods=['POST'])
def score():
    data = request.get_json()
    answers = data.get('answers')
    correct_count = 0
    for word, answer in answers.items():
        if dictionary.meaning(word) is not None and dictionary.synonym(word) is not None and answer.lower() in dictionary.synonym(word):
            correct_count += 1
    score = correct_count / len(answers)
    return "您的得分为：%.2f" % score
