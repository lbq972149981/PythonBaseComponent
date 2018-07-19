#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-25使用扩展库openpyxl读写Excel 2007及更高版本Excel文件
fn = r'D:\Python\abc\test1.xlsx'
wb = openpyxl.workbook.Workbook()
ws = wb.create_sheet(title='Hello World!')
ws['A1'] = '这是第一个单元格'
ws['B1'] = 3.1415926
wb.save(fn)
wb = openpyxl.load_workbook(fn)
ws = wb.worksheets[1]
print(ws['A1'].value)
ws.append([1, 2, 3, 4, 5])
ws.merge_cells('F2:F3')
ws['F2'] = ' = sum(A2:E2)'
for r in range(10, 15):
    for c in range(3, 8):
        _ = ws.merge_cells(row=r, column=c, value=r*c)
wb.save(fn)
 
 
def generateRandomInformation(filename):
    workbook = openpyxl.Workbook()
    worksheet = workbook.worksheets[0]
    worksheet.append(['姓名', '课程', '成绩'])
    first = tuple('赵钱孙李')
    middle = tuple('伟昀琛东')
    last = tuple('坤艳志')
    subjects = ('语文', '数学', '英语')
    for i in range(200):
        line = []
        r = random.randint(1, 100)
        name = random.choice(first)
        if r > 50:
            name = name + random.choice(middle)
        name = name + random.choice(last)
        line.append(name)
        line.append(random.choice(subjects))
        line.append(random.randint(0, 100))
        worksheet.append(line)
    workbook.save(filename)


def getResult(oldfile, newfile):
    result = dict()
    workbook = openpyxl.load_workbook(oldfile)
    worksheet = workbook.worksheets[0]
    for row in worksheet.rows[1:]:
        name, subject, grade = row[0].value, row[1].value, row[2].value
        t = result.get(name, [])
        f = t.get(subject, ())
        if grade > f:
            t[subject] = grade
            result[name] = t
    workbook1 = openpyxl.Workbook()
    worksheet1 = workbook1.worksheets[0]
    worksheet1.append(['姓名', '课程', '成绩'])
    for name, t in result.items():
        for subject, grade in t.items():
            worksheet1.append([name, subject, grade])
    workbook1.save(newfile)


if __name__ == '__main__':
    oldfile = r'D:\Python\abc\test1.xlsx'
    newfile = r'D:\Python\abc\result.xlsx'
    generateRandomInformation(oldfile)
    getResult(oldfile, newfile)