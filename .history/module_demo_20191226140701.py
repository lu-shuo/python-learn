#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'demo'

__author__ = 'Darren Lu'

import sys

# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]
print(sys.argv)

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    test()


# # 作用域
# 通过_前缀来表示仅在模块内部使用的变量或者函数，类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# 只是不应该，而不是不能，python并没有限制访问privat变量