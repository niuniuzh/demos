# coding=utf8
from flask import Flask
from encrypt import encrypted_request
import requests
from flask import request
import hashlib

app = Flask(__name__)

def createRequest(url, data, cookie):
    params = encrypted_request(data)
    headers= {
    #   "Accept":"*/*",
    #   "Accept-Language":"zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4",
    #   "Connection":"keep-alive",
    #   "Content-Type":"application/x-www-form-urlencoded",
    #   "Referer":"http://music.163.com",
    #   "Host":"music.163.com",
    #   "Cookie": cookie,
        'Referer': 'http://music.163.com',
        'Cookie': 'appver=1.5.6',
        "User-Agent":request.headers.get('User-Agent'),
    }
    resp = requests.post(headers=headers,url=url,params=params)
    return resp

@app.route('/test/<key>')
def haha(key):
    print(request.cookies,'xixijalsdjfakgjas')
    return requests.get("http://music.163.com").text

@app.route('/<key>')
def index(key):
    url="http://music.163.com/weapi/login/cellphone"
    password="803312"
    md5sum = hashlib.md5()
    md5sum.update(password.encode(encoding='utf-8'))
    print(md5sum.hexdigest())
    params = dict(
        phone="18680673675",
        password=md5sum.hexdigest(),
        rememberLogin=True
    )
    resp = createRequest(url,params,"")
    print(resp.cookies)
    return resp.text

if __name__ == "__main__":
    app.run(debug=True)
