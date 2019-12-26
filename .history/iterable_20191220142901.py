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
from collections import Iterable
from collections import Iterator

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
print(isinstance((x for x in range(10)), Iterator)) 