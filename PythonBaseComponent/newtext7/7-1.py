# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:47:31 2017

@author: Administrator
"""
s = '文本文件的读取方式\n 文本文件的写入方式\n'
with open('7-1.txt','a+') as f:
    f.write(s)