#coding:utf-8
import re
from datetime import datetime,date
import string
import time

from lib2to3.fixer_util import String
str = "input_1981.10.21.txt"
print(str)
str = re.findall(r"(\d+)",str)
print(str)

b = datetime((int)(str[0]),(int)(str[1]),(int)(str[2]))

print(b)


a = datetime.now().weekday()
print((int)(a)+1)

anyday = datetime((int)(str[0]),(int)(str[1]),(int)(str[2])).strftime("%w")
print((int)(anyday)+1)
w = (int)(anyday)+1
w ='%d' %w

# str0 = time.strftime("%Y-%m-%d-%w",time.localtime())
dat = b
print(dat)
print(dat.strftime('%Y-%m-%d-%w'))
str12 = dat.strftime('%Y-%m-%d-')
str = "output_"+str12+w+".txt"
print(str)

