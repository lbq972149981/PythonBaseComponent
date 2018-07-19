#coding:utf8
'''
Created on 2017年11月4日

@author: Administrator
'''
#threading.activeCount()的使用，此方法返回当前进程中线程的个数。返回的个数中包含主线程。
import threading
import time
 
def worker():
    print ("test")
    time.sleep(1)
 
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
 
print("current has %d threads" % (threading.activeCount() - 1))