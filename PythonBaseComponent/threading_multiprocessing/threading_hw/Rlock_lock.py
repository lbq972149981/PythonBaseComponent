#coding:utf8
'''
Created on 2017年11月4日

@author: Administrator
'''
#线程锁 threading.RLock 和 threading.Lock
# 由于线程之间是进行随机调度，并且每个线程可能只执行n条执行之后，CPU接着执行其他线程。为了保证数据的准确性，引入了锁的概念。
# 所以，可能出现如下问题：假设列表A的所有元素就为0，当一个线程从前向后打印列表的所有元素，另外一个线程则从后向前修改列表的元素为1, 那么输出的时候，列表的元素就会一部分为0，一部分为1,这就导致了数据的不一致。锁的出现解决了这个问题。
import threading  
import time  
globals_num = 0  
lock = threading.RLock()  
  
  
def func():  
    lock.acquire()  # 获得锁  
    global globals_num  
    globals_num += 1  
    time.sleep(1)  
    print(globals_num)  
    lock.release()  # 释放锁  
  
for i in range(10):  
    t = threading.Thread(target=func)  
    t.start()  
    pass  