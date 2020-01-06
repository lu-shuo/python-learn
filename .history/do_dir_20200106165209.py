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