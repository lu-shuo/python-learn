# !/usr/bin/env python
# -*- encoding: utf-8 -*-

'使用__slots__'

__author__ = 'Darren Lu'

from types import MethodType

# class Student(object):
#     def get_self(self):
#         print(self)

# s = Student()

# s.name = 'Darren'

# def set_age(self,age):
#     print(self)
#     self.age = age

# print(s.get_self())
# print(Student)
# 还可以尝试给实例绑定一个方法：
# s.set_age = MethodType(set_age,s)
# s.set_age(23)
# print(s.age)
# a = Student()
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# a.set_age(24)
# print(a.age)

# 为了给所有实例都绑定方法，可以给class绑定方法：
# Student.set_age = set_age
# 给class绑定方法后，所有实例均可调用：
# a.set_age(24)
# print(a.age)
# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

a = Student()

a.name = 'Darren'
a.age = 23
# a.score = 90
print(a.name,a.age)
# print(a.score)
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Goodboy(Student):
    __slots__ = ('score')

b = Goodboy()
b.score = 90
print(b.score)

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。