# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:23:15 2017

@author: Administrator
"""

import difflib
A = open('dir.txt','r')
B = open('dir1.txt','r')
contextA = A.read()
contextB = B.read()
s = difflib.SequenceMatcher(lambda x:x=="",contextA,contextB)
result = s.get_opcodes()
for tag,i1,i2,j1,j2 in result:
    print("%s contextA[%d:%d]=%s contextB[%d:%d]=%s"%(tag,i1,i2,contextA [i1:i2],j1,j2,contextB[j1:j2]))