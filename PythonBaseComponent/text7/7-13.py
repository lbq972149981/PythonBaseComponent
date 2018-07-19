#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
f=open('test.txt','r')
allLinelens = [len(line.strip()) for line in f]
f.close()
longest = max(allLinelens)
print(longest)

f = open('D:\Python\\abc\mydata.txt', 'r')
longest = max(len(line.strip()) for line in f)
f.close()
print(longest, '\n')