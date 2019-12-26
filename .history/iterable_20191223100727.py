#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Untitled-1
@Time    :   2019/12/20 14:18:35
@Author  :   Darren 
@Version :   1.0
@Contact :   734876157@qq.com
@License :   (C)Copyright 2019-2020, Darren
@Desc    :   None
'''

# here put the import lib
from collections.abc import Iterable
from collections.abc import Iterator
import functools
import time

# 可直接作用于for循环的对象统称为可迭代对象：Iterable
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。

# 使用isinstance()判断一个对象是否是Iterable对象：
# print(isinstance([],Iterable))
# print(isinstance({},Iterable))
# print(isinstance('abc',Iterable))
# print(isinstance((x for x in range(10)),Iterable))
# print(isinstance([x for x in range(10)],Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
# print(isinstance((x for x in range(10)), Iterator))
# print(isinstance([],Iterator)) 
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
# print(isinstance(iter([]),Iterator))

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
# for x in [1, 2, 3, 4, 5]:
#     pass

# 完全等价于：

# it = iter([1,2,3,4,5])
# while True:
#     try:
#         x = next(it)
#     except StopIteration:
#         break
def log(text):
    def decorator(func):
        #log(text)(func)后func.__name__已经变成wrapper，用下行代码重新绑定，必写
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('2019-12-23')
def normalize(name):
    return name.capitalize()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
# print(normalize.__name__)
print(time.localtime())
