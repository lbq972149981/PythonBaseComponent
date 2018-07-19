# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:59:58 2017

@author: Administrator
"""

import xlrd
book = xlrd.open_workbook(r'test.xls')
sheet1 = book.sheet_by_name('First')
row0 = sheet1.row(0)
print(row0[0])

print(row0[0].value)