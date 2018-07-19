# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:15:46 2017

@author: Administrator
"""

f = open('7-1.txt','r')
while True:
    line = f.readline()
    if line =='':
        break
    print(line,end='')
f.close()