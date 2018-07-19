# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:28:48 2017

@author: Administrator
"""

x = input('Please input an integer less than 1000:')
x = eval('x')
t = x
i = 2
result = []
while True:
    if t==1:
        break
    if t%i==0:
        result.append(i)
        t = t/i
    else:
        i+=1
Print x,'=','*'.join(map(str,result))