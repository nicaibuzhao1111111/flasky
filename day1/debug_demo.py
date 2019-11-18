#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask

app = Flask(__name__)
# 使用update方法，debug必须大写
app.config.update(DEBUG=True)

@app.route("/")
def hello_world():
    a = 1
    b = 0
    print(a+b)
    return  "Hello World!"


if __name__ == '__main__':
    # app.run(debug=True) # flask自带的测试应用服务器
    app.run()