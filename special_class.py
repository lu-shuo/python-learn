#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'定制类'

__author__ = 'Darren Lu'

# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。



class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
# __str__  自定义print打印的字符串
    def __str__(self):
        return 'Student object (name: %s,age: %d)' % (self.name,self.age)
# __repr__  返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务,通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
    __repr__ = __str__

darren = Student('Darren',23)

print(darren)