# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:26:21 2017

@author: Administrator
"""

s = '中国山东烟台 SDIBT'
fp = open(r'7-4.txt','w')
fp.write(s)
fp.close()
fp = open(r'7-4.txt','r')
print(fp.read(3))
fp.seek(2)
print(fp.read(1))
fp.seek(13)
print(fp.read(1))
fp.seek(15)
print(fp.read(1))
fp.seek(3)
#print(fp.read(1))