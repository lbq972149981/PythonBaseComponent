#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
import re

with open('data.txt','r') as f:
    data = f.readlines()
print(data[0])
data = re.findall(r"(\d+)",data[0])
data.sort()
str = ""
for s in data:
    str = str + s + " "
with open('data_asc.txt','w') as f:
    f.writelines(str)
f.close()

