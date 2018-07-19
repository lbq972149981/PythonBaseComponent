# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:55:49 2017

@author: Administrator
"""

f = open('test.txt','r')
allLineLens = [len(line.strip()) for line in f]
f.close()
longest = max(allLineLens)
print(longest)