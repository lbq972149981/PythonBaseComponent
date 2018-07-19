#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
import zipfile
import sys
# eg. 7-26查看指定xip和rar压缩文件中的文件列表
fp = zipfile.ZipFile(r'D:\Download')
for g in fp.namelist():
    print(f)
fp.close()
   
r = rarfile.RarFile(r'asp网站.rar')
for f in r.namelist():
    print(f)
r.close()