#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/21 10:45
from datetime import datetime

from flask import Flask,render_template
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True # html文件保存后可直接运行，不需要重启服务

@app.route("/")
def index():
    context = {
        "creat_time" : datetime(2019,11,25,15,10,0),
    }
    return render_template("index.html",**context)

@app.template_filter("handle_time")
def handle_time(time):
    """
    time距离现在的时间间隔
    1、如果时间间隔小于1分钟以内，那面就显示刚刚
    2、如果时间间隔大于1分钟，小于1个小时，那么就显示***分钟前
    3、如果大于1小时，小于24小时，那么就显示**小时前
    4、如果大于24小时，小于30天内，那么就显示***天前
    5、否则就显示具体时间
    :param time:
    :return:
    """
    if isinstance(time,datetime):
       now = datetime.now()
       print(now)
       timestamp = (now - time).total_seconds()
       print(timestamp)
       if timestamp < 60:
           return "刚刚"
       elif timestamp >= 60 and timestamp < 60*60:
           minutes = timestamp/60
           return "%s分钟前" % int(minutes)
       elif timestamp >= 60*60 and timestamp < 60*60*24:
           hours = timestamp/(60*60)
           return "%s小时前" % hours
       elif timestamp >= 60*60*24 and timestamp < 60*60*24*30:
           days = timestamp/(60*60*24)
           return "%s天前" % int(days)
       else:
           time.strftime('%Y/%m/%d %H:%M')
    else:
        return time



if __name__ == '__main__':
    app.run(debug=True)
