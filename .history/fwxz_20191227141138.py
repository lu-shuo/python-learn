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
# class Student(object):
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     def print_age(self):
#         print('%s : %s' % (self.__name, self.__age))

# Darren = Student('Darren',23)
# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：
# Darren.name = 'lushuo' #无效
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
# print(Darren.print_age()) #Darren : 23

# 如果外部代码要获取name和score，可以给Student类增加get_name和get_score这样的方法,要修改可以定义set_age这样的方法：
# class Student(object):

#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

#     def print_age(self):
#         print('%s : %s' % (self.__name, self.__age))

#     def get_name(self):
#         return self.__name

#     def get_age(self):
#         return self.__age
# # 你也许会问，原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
#     def set_age(self, age):
#         if isinstance(age,int):
#             self.__age = age
#         else:
#             raise ValueError('Age is Not int')

# darren = Student('darren',23)

# darren.set_age('22')  #抛出错误

# print(darren.get_age())


# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。