# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:28:58 2017

@author: Administrator
"""

x = [i for i in range(1,100) if i%2==1]
print(sum(x))
print(sum(range(1,100)[::2]))