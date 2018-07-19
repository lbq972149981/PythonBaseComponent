#coding:utf8
'''
Created on 2017年11月4日

@author: Administrator
'''
# 守护进程就是不阻挡主程序退出，自己干自己的。 mutilprocess.setDaemon(True)就这句。
# 等待守护进程退出，要加上join，join可以传入浮点数值，等待n久就不等了
import multiprocessing  
import time  
import sys  
  
def daemon():  
    name = multiprocessing.current_process().name  
    print('Starting:', name ) 
    time.sleep(2)  
    print ('Exiting :', name)
  
def non_daemon():  
    name = multiprocessing.current_process().name  
    print('Starting:', name)
    print('Exiting :', name)
  
if __name__ == '__main__':  
    d = multiprocessing.Process(name='daemon',  
                                target=daemon)  
    d.daemon = True  
  
    n = multiprocessing.Process(name='non-daemon',  
                                target=non_daemon)  
    n.daemon = False  
  
    d.start()  
    n.start()  
  
    d.join(1)  
    print('d.is_alive()', d.is_alive()) 
    n.join()  