#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-16比较两个文本文件是否相同
A = open(r'D:\Python\\abc\mydata.txt')
B = open(r'D:\Python\\abc\sample.txt')
contextA = A.read()
contextB = B.read()
s = difflib.SequenceMatcher(lambda x: x==" ", contextA, contextB)
result = s.get_opcodes()
for tag, i1, i2, j1, j2 in result:
    print("%s contextA[%d:%d]=%s contextB[%d:%d]=%s" %\
          (tag, i1, i2, contextA[i1:i2], j1, j2, contextB[j1, j2]))