# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:01:09 2017

@author: Administrator
"""

def Cnil(n,i):
    if not (isinstance(n,int) and isinstance(i,int) and n>=i):
        print('n and i must be integers and n must be larger than or equal to i.')
        return
    result = 1
    Min,Max = min(i,n-i),max(i,n-1)
    for i in range(n,0,-1):
        if i>Max:
            result *= i
        elif i<=Min:
            result /= i
    return result
print (Cnil(6,2))