#coding:utf8
'''
Created on 2017年11月4日

@author: Administrator
'''
#确定当前的进程，即是给进程命名，方便标识区分，跟踪
import multiprocessing  
import time  
def worker():  
    name = multiprocessing.current_process().name
    print(name, 'Starting')  
    time.sleep(2)  
    print(name, 'Exiting')
  
def my_service():  
    name = multiprocessing.current_process().name  
    print(name, 'Starting')  
    time.sleep(3)  
    print (name, 'Exiting')  
  
if __name__ == '__main__':  
    service = multiprocessing.Process(name='my_service',  
                                      target=my_service)  
    worker_1 = multiprocessing.Process(name='worker 1',  
                                       target=worker)  
    worker_2 = multiprocessing.Process(target=worker) # default name  
  
    worker_1.start()  
    worker_2.start()  
    service.start()  