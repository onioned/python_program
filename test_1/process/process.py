# -*- coding: utf-8 -*-
'这是进程的学习'
'''
一个程序至少有一个进程，一个进程至少有一个线程
多进程模式
多线程模式
多进程 + 多线程模式
'''

'''
Process(target ,args ,kwargs,name):创建进程的类
target 表示调用对象
args 表示调用对象的位置参数元组
kwargs表示调用对象的字典
name为别名
group实质上不使用

daemon 属性：让子进程跟随父进程结束
p.daemon = True

join 方法：阻塞当前进程，直到调用 join 方法的那个进程执行完，再继续执行当前进程
p.join()

进程池：
Pool ：批量创建子进程
Pool(num)  num 同时执行进程的数量
p.apply_async(fun, args=(i,))

进程通讯：
Queue、Pipes 


'''

import os;
from multiprocessing import  Process

def run_proc(name):
    print('Child process %s (%s) Running ...' % (name,os.getpid()))

if __name__ == '__main__':
    print('父进程开始-Parent process %s.' % os.getppid())
    for i in range(5):
        p = Process(target=run_proc,args=(str(i),))
        print('Process will start.')
        p.start();
    p.join();
    print('---------------------父进程结束-Process end----------------------')


'''
问题：
先打印，后启动进程，有些慢了。
答案：先执行父进程，后执行子进程
'''

#print('------------------华丽的分割线-------------------')

import multiprocessing
import time

def worker(interval, name):
    print(name + '【start】')
    time.sleep(interval)
    print(name + '【end】')

if __name__ == "__main__":
    #--------------- 子进程
    p1 = multiprocessing.Process(target=worker, args=(2, '两点水1'))
    p2 = multiprocessing.Process(target=worker, args=(3, '两点水2'))
    p3 = multiprocessing.Process(target=worker, args=(4, '两点水3'))
    p1.daemon = True        #父进程关闭，子进程则关闭
    p1.start()
    p2.start()
    p3.start()
    # --------------- 子进程 end

    # --------------- 主进程区域
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print("END!!!!!!!!!!!!!!!!!")
    # --------------- 主进程区域 end

'''
    #先执行父进程，后执行子进程
'''

from multiprocessing import Pool
import os,time,random

def run_task(name):
    print('Task %s (pid = $s) is running ...' % (name,os.getpid()));
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)

if __name__ == '__main__':
    print('当前的进程 %s .' % os.getppid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close();
    p.join();
    print('All subprocesses done.')

