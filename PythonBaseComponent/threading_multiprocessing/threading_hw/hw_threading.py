#coding:utf8
'''
Created on 2017年11月4日

@author: Administrator
'''
import threading
import time
 
def worker():
    str = "worker"
    time.sleep(1)
    return
def runTimeTesterth():
    startTime = time.time()
    threadFunction()
    runTime = time.time() - startTime   #calculate runtime
    return format(runTime)
def runTimeTesterFun():
    startTime = time.time()
    Function()
    runTime = time.time() - startTime   #calculate runtime
    return format(runTime)
def format(old):
    new = old
    return '{:.5f}'.format(new)
def threadFunction():
    for i in range(5):
        t = threading.Thread(target=worker)
        t.start()
def Function():
    for i in range(5):
          worker()
if __name__ == '__main__':
    print(runTimeTesterth(),runTimeTesterFun())
    
