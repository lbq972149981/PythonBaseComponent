# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:49:57 2017

@author: Administrator
"""

import xlwt

book = xlwt.Workbook()
sheet1 = book.add_sheet("First")
al = xlwt.Alignment()
al.horz = xlwt.Alignment.HORZ_CENTER
al.vert = xlwt.Alignment.VERT_CENTER
borders = xlwt.Borders()
borders.bottom = xlwt.Borders.THICK
style = xlwt.XFStyle()
style.alignment = al
style.borders = borders
row0 = sheet1.row(0)
row0.write(0,'test',style = style)
book.save(r'test.xls')