# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:06:07 2017

@author: Administrator
"""

def is_gif(fname):
    f = open(fname,'r')
    first4 = tuple(f.read(4))
    f.close()
    return first4==('G','I','F','8')

print(is_gif('test.txt'))