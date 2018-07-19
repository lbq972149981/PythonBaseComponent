# -*- coding: utf-8 -*-e
"""
Created on Thu Oct 26 22:11:41 2017

@author: Administrator
"""

filename = '7-6.py'
with open(filename,'r') as fp:
    lines = fp.readlines()
lines = [line.rstrip() + ' '*(100-len(line)) + '#' + str(index) + '\n' for index,line in enumerate(lines)]
with open(filename[:-3] + '_new.py','w') as fp:
    fp.writelines(lines)
