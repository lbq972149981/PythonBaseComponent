#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-19使用Pywin32操作Excel文件
xlApp = win32com.client.Dispatch('Excel.Application')
xlBook = xlApp.Workbooks.Open(r'D:\Python\\abc\\test.xls')
xlSht = xlBook.Worksheets('sheet1')
aaa = xlSht.Cells(1, 2).Value
xlSht.Cells(2, 3).Value = aaa
xlBook.Close(SaveChanges=1)
del xlApp