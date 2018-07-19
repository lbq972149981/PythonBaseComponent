#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
filename = 'hell.py'
with open(filename,'r') as f:
    lines = f.readlines()
    print(lines)
lines = [line.rstrip()+' '*(100-len(line))+'#'+str(index)+'\n' for index ,line in enumerate(lines)]
with open(filename[:-3]+'_new.py','w') as f:
    f.writelines(lines)
f.close()