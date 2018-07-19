#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
import zlib
import binascii
print(zlib.crc32('1234'.encode()))
print(zlib.crc32('111'.encode()))
print(zlib.crc32('SDIBT'.encode()))
print(binascii.crc32('SDIBT'.encode()))
