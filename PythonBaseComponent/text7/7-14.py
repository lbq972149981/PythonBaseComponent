#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-14计算字符串MD5值
md5value = hashlib.md5()
md5value.update('12345'.encode())
md5value = md5value.hexdigest()
print(md5value)
md5value = _md5.md5()
md5value.update('12345'.encode())
md5value = md5value.hexdigest()
print(md5value, '\n')