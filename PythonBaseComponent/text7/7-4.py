#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
s='中国山东烟台 SDIBT'
f=open(r'sample.txt','w')
f.write(s)
f.close()
f=open(r'sample.txt','r')
print(f.read(3))
f.seek(2)
f.close()