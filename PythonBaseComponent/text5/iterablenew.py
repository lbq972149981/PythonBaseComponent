#coding:utf8
'''
Created on 2017年10月27日

@author: Administrator
'''
#Initialize bound of the size.
size = 100000
#import time module to calculate time
import time,sys
def format(old):
    new = old
    return '{:.5f}'.format(new)  
#计时器
def runTimeTester(func,*args):
    startTime = time.time()
    for eachFunc in range(size):
        func(*args)
        runTime = time.time() - startTime   #calculate runtime
        return format(runTime)
#迭代器
# def it(res):
#     it = iter(res)
#     while True:
#         try:
#             # 获得下一个值:
#             x = next(it)
#         except StopIteration:
#             # 遇到StopIteration就退出循环
#             break
#for循环
def forLoop():
    res = []
    for x in range(size):
        res.append(x**2)
#     it(res)

#列表解析
def listComprehension():
    res = [x**2 for x in range(size)]
#     it(res)
#生成表达式
def generatorExpression():
    res = (x**2 for x in range(size))
#     it(res)
def generatorFunction():
    def add(x):
        yield x**2;
    res = [add(x) for x in range(size)]
#     it(res)
#map函数
def mapFunction():
    res = list(map(lambda x:x**2,range(size)))
#     it(res)
#测试
if __name__ == '__main__':
    func = [forLoop,listComprehension,generatorExpression,generatorFunction,mapFunction]
    for eachFunc in func:
        print(eachFunc.__name__.ljust(20),">>",runTimeTester(eachFunc))