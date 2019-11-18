#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return  "Hello World!"

@app.route("/list/")
def artocle_list():
    return  "artocl list!"

@app.route("/artocle/<artocle_id>")
def artocle_detall(artocle_id):
    return  "您请求的文章是 %s! " % artocle_id


@app.route("/d/")
def d():
    wd = request.args.get("wd")
    ie = request.args.get("ie")
    return "您通过查询字符串的方式传递的参数 %s & %s" % (wd,ie)




if __name__ == '__main__':
    app.run(debug=True) # flask自带的测试应用服务器
