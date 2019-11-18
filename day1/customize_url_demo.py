#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask,url_for
from werkzeug.routing import BaseConverter
app = Flask(__name__)
class TelephoneConveter(BaseConverter):
    regex = r"1[85734]\d{9}"

app.url_map.converters["tel"] = TelephoneConveter


@app.route("/")
def hello_world():
    return  "Hello World!"

@app.route("/user/<int:user_id>")
def user_profile(user_id):
    return "您输入的user_id为：%s" % user_id


@app.route("/telephone/<tel:my_tel>/")
def my_tel(my_tel):
    return "my tel %s" % my_tel






if __name__ == '__main__':
    app.run(debug=True) # flask自带的测试应用服务器
