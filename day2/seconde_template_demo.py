#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/18 15:23

from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index2.html",username="你猜不着",age=18,country="china")

@app.route("/dic/")
def dic():
    context = {
        "user":"你猜不着",
        "age":18,
        "country":"china"

    }
    return render_template("index2.html",context=context)

@app.route("/dic2/")
def dic2():
    context = {
        "user":"你猜不着",
        "age":18,
        "country":"china",
        "names":{
            "boys":"lili",
            "girls":"hanmeimei"
        }

    }
    return render_template("index2.html",**context)#python知识点，双星号表示将字典转换成关键字参数，key=value


if __name__ == '__main__':
    app.run(debug=True)