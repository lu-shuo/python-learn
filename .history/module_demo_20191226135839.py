#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'demo'

__author__ = 'Darren Lu'

import sys

# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
print(sys.argv)

def func(*args):
    print('hello,',args)

if __name__=='__main__':
    func(*sys.argv)