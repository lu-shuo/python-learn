#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'多进程'

__author__ = 'Darren Lu'

import multiprocessing as mp
import os

# print(os.getpid())
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = mp.Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')