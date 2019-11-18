#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask,Response,jsonify,url_for
app = Flask(__name__)

class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        """
        这个方法是有视图函数返回非字符、非元组、非response对象才会调用
        response 视图函数的返回值
        :param response:
        :param environ:
        :return:
        """
        if isinstance(response,dict):
            response = jsonify(response)
        return Response("HELLO")

@app.route("/")
def hello_world():
    return  "Hello World!"

@app.route("/list1/")
def list1():
    return "这是list1"


if __name__ == '__main__':
    app.run(debug=True) # flask自带的测试应用服务器
