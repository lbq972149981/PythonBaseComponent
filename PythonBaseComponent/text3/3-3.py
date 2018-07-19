#-*-coding:utf-8-*-
import time#访问time模块
def demo(year,month,day) :
    day_month=[31,28,31,30,31,30,31,31,30,31,30,31]#每个月的天数
    if year% 400==0 or (year% 4==0 and year% 100!=0):#判断是否为闰年
        day_month[1]=29                               #闰年2月为29天
    if month==1:
            return day
    else:
            return sum(day_month[:month-1]) +day#切片函数，步长是month-1

date=time.localtime()
year,month,day=date[:3]#切片函数
print(demo(year,month,day))