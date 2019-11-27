# -*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: flasky
# @Time : 2019/11/27 17:15


books = [{
    "name": "三国演义",
    "author": "罗贯中",
    "price": 114
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
        "price": 111
    }
]

for i in books:
    print(i["name"])
    print(i["author"])
    print(i["price"])
