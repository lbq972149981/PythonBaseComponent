# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:17:47 2017

@author: Administrator
"""

import zlib
print(zlib.crc32('1234'.encode()))
print(zlib.crc32('111'.encode()))
print(zlib.crc32('SDIBT'.encode()))
import binascii
print(binascii.crc32('SDIBT'.encode()))