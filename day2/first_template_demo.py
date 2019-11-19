#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask,render_template
# app = Flask(__name__,template_folder=r"D:\templates")
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True) # flask自带的测试应用服务器