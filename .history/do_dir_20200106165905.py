#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'操作文件目录'

__author__ = 'Darren Lu'

# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

# 如果要在Python程序中执行这些目录和文件的操作怎么办？
# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

import os

print(os.name)  #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。


# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
# print(os.environ)
# print(os.environ.get('PATH'))


# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.mkdir('D:\learn\Python\\testdir')
# os.rmdir('D:\learn\Python\\testdir')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：

# part-1/part-2
# 而Windows下会返回这样的字符串：

# part-1\part-2
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

# >>> os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

# >>> os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')