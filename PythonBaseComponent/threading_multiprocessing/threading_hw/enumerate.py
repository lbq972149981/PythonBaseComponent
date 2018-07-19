#coding:utf8
'''
Created on 2017年11月4日

@author: Administrator
'''
#threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表
import threading
import time
 
def worker():
    print("test")
    time.sleep(2)
 
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
 
for item in threading.enumerate():
    print(item)
 
print()
 
for item in threads:
    print (item)