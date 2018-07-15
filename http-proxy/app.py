# coding=utf8
from flask import Flask
from encrypt import encrypted_request
import requests
from flask import request
#  from flask import make_response

app = Flask(__name__)

@app.route('/<key>')
def index(key):
    url="http://music.163.com/weapi/search/get"
    header = {'User-Agent': request.headers.get('User-Agent') }
    params = dict(
        s=key,
        type=1,
        offset=0,
        limit=20
    )
    params = encrypted_request(params)
    resp = requests.post(headers=header,url=url,params=params)
    #  response = make_response(resp.text)
    #  response.headers['Access-Control-Allow-Origin'] = '*'
    #  response.headers['Access-Control-Allow-Methods'] = 'GET'
    #  response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    #  return response
    return resp.text

if __name__ == "__main__":
    app.run(debug=True)
