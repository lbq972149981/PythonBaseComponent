#-*-coding:utf-8-*-
import time#����timeģ��
def demo(year,month,day) :
    day_month=[31,28,31,30,31,30,31,31,30,31,30,31]#ÿ���µ�����
    if year% 400==0 or (year% 4==0 and year% 100!=0):#�ж��Ƿ�Ϊ����
        day_month[1]=29                               #����2��Ϊ29��
    if month==1:
            return day
    else:
            return sum(day_month[:month-1]) +day#��Ƭ������������month-1

date=time.localtime()
year,month,day=date[:3]#��Ƭ����
print(demo(year,month,day))