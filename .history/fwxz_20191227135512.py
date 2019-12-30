#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'访问限制'

__author__ = 'Darren Lu'

# 从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：
# class Student(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def print_age(self):
#         print('%s : %s' % (self.name, self.age))

# Darren = Student('Darren',23)

# Darren.name = 'lushuo'

# print(Darren.print_age()) # lushuo : 23

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def print_age(self):
        print('%s : %s' % (self.__name, self.__age))