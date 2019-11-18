#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask,url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(url_for("my_list",page=1))
    return  "Hello World!"

@app.route("/list/<page>/")
def my_list(page):
    return "my list %s" % page


if __name__ == '__main__':
    app.run(debug=True) # flask自带的测试应用服务器
