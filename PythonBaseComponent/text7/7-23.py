#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-23统计指定目录所有C++源程序文件中不重复代码行数
AllLines = []
NotRepeatedLines = []
file_num = 0
code_num = 0
def LinesCount(directory):
    global AllLines
    global NotRepeatedLines
    global file_num
    global code_num
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            LinesCount(temp)
        elif temp.endswith('.cpp'):
            file_num += 1
            with open(temp, 'r') as fp:
                line = fp.readline()
                if not line:
                    break
                if line not in NotRepeatedLines:
                    NotRepeatedLines.append(line)
                code_num += 1
    return code_num, len(NotRepeatedLines)


path = r'D:\Ccodes'
print("代码总行数:{0[0]}, 非重复代码行数:{0[1]}".format(LinesCount(path)))
print("文件数量:{0}".format(file_num), '\n')