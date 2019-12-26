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

# 可直接作用于for循环的对象统称为可迭代对象：Iterable
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。

# 使用isinstance()判断一个对象是否是Iterable对象：
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))