# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:02:07 2017

@author: Administrator
"""

import sys
from win32com import client

filename = r'test.doc'
word = client.Dispatch('Word.Application')
doc = word.Documents.Open(filename)
content = str(doc.Content)
doc.Close()
word.Quit()

repeatedWords = []
lens = len(content)
for i in range(lens-2):
    ch = content[i]
    ch1 = content[i+1]
    ch2 = content[i+2]
    if (u'\u4e00'<=ch<=u'\u9fa5' or ch in ('，','。','、')):
        if ch == ch1 and ch + ch1 not in repeatedWords:
            print(ch+ch1)
            repeatedWords.append(ch+ch1)
        elif ch==ch2 and ch + ch1 + ch2 not in repeatedWords:
            print(ch+ch1+ch2)
            repeatedWords.append(ch + ch1 + ch2)