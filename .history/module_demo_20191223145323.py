#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'demo'

__author__ = 'Darren Lu'

import sys

print(sys.argv)

def func(text='world'):
    print('hello',text)
    
if __name__=='__main__':
    func(sys.argv[1])