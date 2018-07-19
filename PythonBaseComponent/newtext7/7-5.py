# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:48:18 2017

@author: Administrator
"""

with open('data.txt','r') as fp:
    data = fp.readlines()
data = [int(line.strip()) for line in data]
data.sort()
data = [str(i) + '\n' for i in data]
data.sort()
data = [str(i) + '\n' for i in data]
with open('data_asc.txt','w') as fp:
    fp.writelines(data)