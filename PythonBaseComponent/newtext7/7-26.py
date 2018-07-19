# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:27:07 2017

@author: Administrator
"""
import zipfile
fp = zipfile.ZipFile('r'zipfile.zip'')
for f in fp.namelist():
    print(f)
fp.close()