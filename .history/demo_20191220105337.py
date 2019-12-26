#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo.py
@Time    :   2019/12/18 17:08:48
@Author  :   Darren 
@Version :   1.0
@Contact :   734876157@qq.com
@License :   (C)Copyright 2019-2020, Darren
@Desc    :   None
'''

# here put the import lib
from collections.abc import Iterable

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def trim(s):
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s

#myDict = {'name':'lushuo','age':23,'job':'coder'}
# for key,value in myDict.items():
#     print(key,value)
#print(isinstance([1,2,3],Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对
#for i,value in enumerate(['A','B','C']):
    #print(i,value)

#张辉三角
# 1
# 11
# 121
# 1331
# 14641
def triangle(max):
    yield([1])
    L = [1,1]
    yield(L)
    n = 0
    while n < max:
        L1 = [1]
        for i in range(1,len(L)):
            L1.append(L[i-1]+L[i])
        L1.append(1)
        L = L1
        yield(L1)
        n = n + 1

for n in triangle(5):
    print(n)

