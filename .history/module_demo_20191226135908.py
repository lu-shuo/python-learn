#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'demo'

__author__ = 'Darren Lu'

import sys

# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
print(sys.argv)

def func(*args):
    print('hello,',args)

if __name__=='__main__':
    func(*sys.argv)