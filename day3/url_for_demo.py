#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/20 14:48

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/")
def login():
    return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)