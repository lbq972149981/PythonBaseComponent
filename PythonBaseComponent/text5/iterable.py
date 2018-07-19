#coding:utf8
'''
Created on 2017年10月27日

@author: Administrator
'''
import timeit 
# 首先获得Iterator对象:
def list():
    it = iter([1, 2, 3, 4, 5])
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
            print(x)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break
def set():
    it = iter((x for x in range(5)))
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
            print(x)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break
def add100(x):
    return x+100
def map():
    hh = [11,22,33]
    it = iter(map(add100,hh))
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
            print(x)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break
if __name__=='__main__':
    t1 = timeit.Timer('list()')  
    print(t1.timeit())
    t2 = timeit.Timer('set()')  
    print(t2.timeit())
    t2 = timeit.Timer('map()')  
    print(t2.timeit())