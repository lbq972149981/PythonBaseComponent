#coding:utf-8
import threading
import time
import os
def buyticket(self):
    global count
    global lock
    while(1):
        lock.acquire()
        if count!=0:
            print("售票中...")
            print("剩余票数：",count)
            print()
            count=count-1
            time.sleep(0.2)
        else:
            print("票售完")
            os._exit(0)
        lock.release()
        time.sleep(1)
def run():
    for k in range(10):
        new_thread = threading.Thread(target=buyticket,args=(k,))
        new_thread.start()
if __name__ == '__main__':
    count = 100
    lock = threading.Lock()
    run()