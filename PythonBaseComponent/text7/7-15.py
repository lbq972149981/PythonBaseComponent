#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-15判断一个文件是否为GIF图像文件
def is_gif(fname):
    f1 = open(fname, 'rb')  # 书上是‘r’???
    first4 = tuple(f1.read(4))
    f1.close()
    return first4 == ('G', 'I', 'F', '8')


print(is_gif('D:\Python\\abc\picture1.jpg'), '\n')