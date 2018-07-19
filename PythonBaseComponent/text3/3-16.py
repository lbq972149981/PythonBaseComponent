# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:06:10 2017

@author: Administrator
"""

def licai(base,rate,days):
    result = base
    times = 365//days
    for i in range(times):
        result = result + result * rate/365 * days
    return result
print(licai(100000,0.0385,14))