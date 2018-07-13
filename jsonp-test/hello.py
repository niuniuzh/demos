# coding=utf8
from flask import Flask
app = Flask(__name__)

@app.route('/<cb>')
def index(cb):
    return cb + '({"result":"我是远程的数据"});'

if __name__ == '__main__':
    app.run(debug=True)
