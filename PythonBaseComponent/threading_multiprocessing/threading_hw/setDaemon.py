#coding:utf8
'''
Created on 2017年11月4日

@author: Administrator
'''
#threading.setDaemon()的使用。设置后台进程。
#create a daemon
import threading
import time
 
def worker():
    time.sleep(3)
    print("worker")
 
t=threading.Thread(target=worker)
t.setDaemon(True)
t.start()
print("haha")
#可以看出worker（）方法中的打印操作并没有显示出来，说明已经成为后台进程。