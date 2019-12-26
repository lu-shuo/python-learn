#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'demo'

__author__ = 'Darren Lu'

import sys

print(sys.argv)

def func(*args):
    print('hello,',args)

if __name__=='__main__':
    func(*sys.argv)