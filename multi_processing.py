#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'多进程'

__author__ = 'Darren Lu'

import multiprocessing as mp
import threading as td
import os
import time


# print(os.getpid())
# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# def job_1(q):
#     res = 0
#     for i in range(1000000):
#         res += i + i**2 + i**3
#     q.put(res)

# def job_2(q):
#     res = 0
#     for i in range(500):
#         res += i + i**2 + i**3
#     q.put(res)

# def multicore():
#     q = mp.Queue()
#     t1 = mp.Process(target=job_1, args=(q,))
#     t2 = mp.Process(target=job_1, args=(q,))
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()
#     res1 = q.get()
#     res2 = q.get()
#     # print(res1)
#     # print(res2)
#     print('multicore:', res1 + res2)
    

# def normal():
#     res = 0
#     for j in range(2):
#         for i in range(1000000):
#             res += i + i**2 + i**3
#     print('normal:', res)
#     

# def multithread():
#     # 可以用多进程的queue放到多线程里
#     q = mp.Queue()
#     p1 = td.Thread(target=job_1, args=(q,))
#     p2 = td.Thread(target=job_1, args=(q,))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     # print(res1)
#     # print(res2)
#     print('multithread:', res1 + res2)
 

# 进程池pool,将任务放进去会自动分配进程核心
def pool_job(x):
    # pool里有返回值
    res = 0
    res += x**2
    return res

def multipool():
    # processes指定所用核心数量
    st = time.time()
    print('开始:', time.asctime( time.localtime(time.time()) ))
    pool = mp.Pool(processes = 1)
    res = pool.map(pool_job,range(100))
    print(res)
    st2 = time.time()
    print('结束:', time.asctime( time.localtime(time.time()) ))
    print('用时：%0.5f s' % (st2 - st) )
    # 一个进程计算单一值，只能接受一个参数
    # res = pool.apply_async(pool_job, (2,))
    # print(res)
    # print(res.get())
    # multi_res = [pool.apply_async(pool_job, (i,)) for i in range(10)]
    # print([res.get() for res in multi_res])

if __name__=='__main__':
    # st_1 = time.time()
    # normal()
    # print('normal time: %.5f' % (time.time() - st_1))
    # st_2 = time.time()
    # multicore()
    # print('multicore time: %.5f' % (time.time() - st_2))
    # st_3 = time.time()
    # multithread()
    # print('multithread time: %.5f' % (time.time() - st_3))
    multipool()

