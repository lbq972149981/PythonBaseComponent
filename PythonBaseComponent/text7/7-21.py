#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
# eg. 7-21编写程序，进行文件夹增量备份
import os
import sys
import shutil
import filecmp
import CopyDir

def autoBackup(scrDir, dstDir):
    if(not os.path.isdir(scrDir)) or (not os.path.isdir(dstDir)) or ( os.path.abspath(scrDir) 

!= scrDir) or (os.path.abspath(dstDir) != dstDir):
        usage()
    for item in os.listdir(scrDir):
        scrItem = os.path.join(scrDir, item)
        dstItem = scrItem.replace(scrDir, dstDir)
        if os.path.isdir(scrItem):
            if not os.path.exists(dstItem):
                os.makedirs('make directory' + dstItem)
                print('make directory' + dstItem)
            autoBackup(scrItem, dstItem)
        elif os.path.isfile(scrItem):
            if (not os.path.exists(dstItem)) or (not filecmp.cmp(scrItem, dstItem, 

shallow=False)):
                shutil.copyfile(scrItem, dstItem)
                print('file:'+scrItem+'==>'+dstItem)


def usage():
    print('scrDir and dstDir mustbe existing absoltue path of certain directory')
    print('For example: {0} c:\\olddir c:\\newdir'.format(sys.argv[0]))
    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
    scrDir, dstDir = sys.argv[1], sys.argv[2]
    autoBackup(scrDir, dstDir)