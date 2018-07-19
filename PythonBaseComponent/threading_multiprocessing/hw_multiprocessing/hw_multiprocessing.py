#coding:utf8
'''
Created on 2017年11月4日

@author: Administrator
'''
#简单创建进程
import multiprocessing 
def worker(num):  
    """thread worker function"""  
    print('Worker:', num)
    return  
  
if __name__ == '__main__':  
    jobs = []  
    for i in range(5):  
        p = multiprocessing.Process(target=worker, args=(i,))  
        jobs.append(p)  
        p.start()  