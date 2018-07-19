# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:41:00 2017

@author: Administrator
"""

import hashlib
#import md5
md5value = hashlib.md5()
md5value.update('12345'.encode())
md5value = md5value.hexdigest()
print(md5value)

'''md5value = md5.md5()
md5value.update('12345'.encode())
md5value = md5value.hexdigest()
print(md5value)'''