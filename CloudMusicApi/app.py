# coding=utf8
from flask import Flask
from encrypt import encrypted_request
import requests
from flask import request
import hashlib
import time
from requests import exceptions
import math
import random

app = Flask(__name__)

def randomString(pattern, length):
    temp = []
    for i in map(lambda x: pattern[math.floor(random.random() * len(pattern))], list(range(length))):
        temp.append(i)
    return ''.join(temp)

jsessionid = randomString('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ\\/+',176) + ':' + str(time.time())
nuid = randomString('0123456789abcdefghijklmnopqrstuvwxyz',32)
baseCookie='JSESSIONID-WYYY=' + str(jsessionid) + '; _iuqxldmzr_=32; _ntes_nnid=' + str(nuid) + ',' + str(time.time()) + '; _ntes_nuid=' + str(nuid)

def createRequest(url, data, cookie):
    params = encrypted_request(data)
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "http://music.163.com",
        "Host": "music.163.com",
        "Cookie": cookie,
        "User-Agent": request.headers.get('User-Agent'),
    }
    try:
        start = time.time()
        resp = requests.post(
            headers=headers, url=url, params=params, timeout=5)
        resp.raise_for_status()
        end = time.time()
    except exceptions.Timeout:
        print('请求超时')
    except exceptions.HTTPError:
        print('http请求错误')
    else:
        print('请求耗时%ss' % (end - start))
        if resp.status_code == 200:
            print(resp.cookies)
            return resp
        else:
            resp.status_code = 502
            resp.text = 'feach error'
            return resp


@app.route('/<key>')
def index(key):
    url = "http://music.163.com/weapi/login/cellphone"
    password = "803312"
    md5sum = hashlib.md5()
    md5sum.update(password.encode(encoding='utf-8'))
    params = dict(
        phone="18680673675", password=md5sum.hexdigest(), rememberLogin=True)
    cookie = baseCookie + ';' + request.cookies.__str__()
    print(cookie)
    print(request.cookies.__str__())
    resp = createRequest(url, params, cookie)
    return resp.text

@app.route('/album')
def album():
    pass

if __name__ == "__main__":
    app.run(debug=True)
