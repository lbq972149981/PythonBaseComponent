#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg.7-24递归删除指定文件夹中指定类型文件
filetypes = ['.tmp', '.log', '.obj', '.txt']


def delCertainFiles(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)
        elif splitext(temp)[1] in filetypes:
            remove(temp)
            print(temp, 'deleted.…')


def main():
    directory = r'D:\Python\abc\xyz'
    # directory = sys.argv[1]
    delCertainFiles(directory)

main()