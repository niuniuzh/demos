# 使用代理解决跨域Demo
浏览器请求有跨域限制，服务器请求没有限制，服务器做代理，将
请求数据返回浏览器端。

## 安装依赖
Demo使用的网易云音乐搜索接口，使用flask框架，和[musicbox](https://github.com/darknessomi/musicbox)加密部分.
```
pip install flask,requests,pycryptodomex,future
```

## 使用方法
下载项目，切到http-proxy目录，安装依赖,运行后台，然后访问index.html.
输入要查询的歌曲，或者歌手名称.
```
git clone git@github.com:niuniuzh/demos.git
cd http-proxy
pip install requirements.txt
python hello.py
```
