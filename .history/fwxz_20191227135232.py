#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'访问限制'

__author__ = 'Darren Lu'

# 从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_age(self):
        print('%s : %s' % (self.name, self.age))

Darren = Student(Darren,23)

print(Darren.print_age)
