#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
fp=open('simple.txt','r')
print(fp.read(5))
print(fp.read(7))
print(fp.read(9))
fp.close()
