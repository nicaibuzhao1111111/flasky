#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask
# 创建一个Flask对象，传递一个__name__参数进去
app = Flask(__name__)


# @app.route() 是一个装饰器
# @app.route("/") 将url中的/ 映射到 hello_world视图函数上
@app.route("/")
def hello_world():
    return  "Hello World!"


if __name__ == '__main__':
    app.run() # flask自带的测试应用服务器