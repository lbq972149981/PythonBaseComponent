#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''

# eg. 7-17使用xlwt模块写入Excel文件
book = Workbook()
sheet1 = book.add_sheet("First")
al = Alignment()
al.horz = Alignment.HORZ_CENTER
al.vert = Alignment.VERT_CENTER
borders = Borders()
borders.bottom = Borders.THICK
style = XFStyle()
style.alignment = al
style.borders = borders
row0 = sheet1.row(0)
row0.write(0, 'test', style=style)
book.save(r'D:\\Python\\abc\test.xls')
