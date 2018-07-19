#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# f=open('simple.txt','r')
# while True:
#     line=f.readline()
#     if line =="":
#         break
#     print(line,end="")
# f.close()
f=open('simple.txt','r')
li = f.readlines()
for line in li:
    print(line,end='')
f.close()