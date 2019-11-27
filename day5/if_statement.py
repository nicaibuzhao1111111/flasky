#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/27 16:32

from flask import Flask,render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
@app.route("/")
def index():
    context = {
        "users":["ni1","ni2","ni3"],
        "person":
            {
                "name":"你猜",
                "age":18,
                "contry":"china"
            },
        "books":[{
                    "name":"三国演义",
                    "author":"罗贯中",
                    "price":114
                },
                {
                    "name": "西游记",
                    "author": "吴承恩",
                    "price": 113
                },
                {
                    "name": "红楼梦",
                    "author": "曹雪芹",
                    "price": 112
                },
                {
                    "name": "水浒传",
                    "author": "施耐庵",
                    "price":111
                }
            ]
        }
    return render_template("index.html",**context)

if __name__ == '__main__':
    app.run(debug=True)