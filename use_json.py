#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'JSON'

__author__ = 'Darren Lu'

# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
# 但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

import json

# d = dict(name = 'darren', age = 23, job = 'coder')
# # dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# print(json.dumps(d))
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))

# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：

# Writing JSON data
# data = dict(name = 'darren', age = 23, job = 'coder')
# with open('./data.json', 'w') as f:
#     json.dump(data, f)

# Reading data back
# with open('./data.json', 'r') as f:
#     data = json.load(f)
# print(data)

# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。




# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

# darren = Student('Darren', 23, 90)
# 不过直接将类序列化是肯定不行的，会报TypeError,需要先将class转化成dict，再序列化
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
# d = json.dumps(darren,default=lambda obj: obj.__dict__)
# 也可以自定义转换函数
# def classToDict(classArg):
#     return {
#         'name': classArg.name,
#         'age': classArg.age,
#         'score': classArg.score
#     }

# d = json.dumps(darren,default=classToDict)
# print(d) 

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# def dictToClass(d):
#     return Student(d['name'], d['age'], d['score'])
# print(json.loads(json_str, object_hook=dictToClass))