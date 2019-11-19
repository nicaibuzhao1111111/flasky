#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask,Response,jsonify
app = Flask(__name__)

# 将视图函数中返回的字典，转换成json对象，然后返回
class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        """
        这个方法是有视图函数返回非字符、非元组、非response对象才会调用
        response 视图函数的返回值
        """
        # 判断response是否为字典，如果是，则使用jsonify转化为json对象
        if isinstance(response,dict):
            # jsonify()：将字典对象转化为json字符串，Content-Type: application
            # json：json.dumps()将字典对象转化为json字符串 , Content-Type: text/html
            # jsonify()除了将字典转化成json对象，还将对象包装成了一个Response对象
            response = jsonify(response)
        elif isinstance(response,list):
            response = str(response)
        return super(JSONResponse,cls).force_type(response,environ)# python 函数知识点， super继承父类

app.response_class = JSONResponse

@app.route("/")
def hello_world():
    return  "Hello World!"

@app.route("/list1/")
def list1():
    res =  Response("这是list1")
    res.set_cookie("country","china")
    return res
@app.route("/list3/")
def list3():
    return {"name":"xiazi","age":12}





if __name__ == '__main__':
    app.run(debug=True) # flask自带的测试应用服务器
