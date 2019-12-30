#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'面向对象'

__author__ = 'Darren Lu'

# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
# 面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))

# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。

# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。

# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

# 数据封装、继承和多态是面向对象的三大特点



# 1.类和实例
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

# class Student(object):
#     pass

# 在Python中，定义类是通过class关键字,class后面是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 定义好了Student类，就可以根据Student类创建出Student的实例
bart = Student()
print(bart)
print(Student)

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定
bart.name = 'Bart Simpson'

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score