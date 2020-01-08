#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'多线程'

__author__ = 'Darren Lu'

import threading
import time
from queue import Queue

# def thread_job():
#     print('This is an added Thread,name is %s' % threading.current_thread())

# def thread_job_1():
#     print('T1 start\n')
#     for i in range(10):
#         time.sleep(0.1)
#     print('T1 finished\n')
    
# def thread_job_2():
#     print('T2 start\n')
#     for i in range(2):
#         time.sleep(0.1)
#     print('T2 finished\n')



# def main():
#     # # 查看当前激活线程数量
#     # print(threading.active_count())
#     # # 查看线程
#     # print(threading.enumerate())
#     # # 当前程序线程
#     # print(threading.current_thread())
#     # 添加线程
#     add_thread = threading.Thread(target=thread_job_1,name='T1')
#     add_thread_2= threading.Thread(target=thread_job_2,name='T2')
    
#     add_thread.start() #开始运行
    
#     add_thread.join() #等待当前线程执行完再执行后续语句
#     add_thread_2.start()
#     add_thread_2.join()
#     print('All done\n')





# Queue:多线程的任务是没有返回值的，运算出的结果需要放在长队列中，在每一个线程的队列到主线程之后再拿出做后续运算。

# def job(l,q):
#     for i in range(len(l)):
#         l[i] = l[i]**2
#     q.put(l)


# def multithreading():
#     q = Queue()
#     threads = []
#     results = []
#     data = [[2,2,2],[3,3,3],[4,4,4],[5,5,5]]
#     for i in range(4):
#         t = threading.Thread(target=job,args=(data[i], q))
#         t.start()
#         threads.append(t)
#     print(threading.active_count())
#     print(threading.current_thread())
#     for thread in threads:
#         thread.join()
#     for _ in range(4):
#         results.append(q.get())
#     print(results)



# Lock: 在线程间使用共享内存时使用
def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()

def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()
    
    

if __name__== '__main__':
    # multithreading()
    A = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()



