#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask,request,redirect,url_for
app = Flask(__name__)

@app.route("/")
def hello_world():
    return  "Hello World!"

@app.route("/login/")
def login():
    return "这是登录页面"

@app.route('/profile/')
def profile():
    if request.args.get("name"):
        return "这是个人中心"
    else:
        return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True) # flask自带的测试应用服务器
