#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-18使用xlrd模块读取Excel文件
book = xlrd.open_workbook(r'D:\Python\abc\test.xls')
sheet1 = book.sheet_by_name('First')
row0 = sheet1.row(0)
print(row0[0])
print(row0[0].value, '\n')