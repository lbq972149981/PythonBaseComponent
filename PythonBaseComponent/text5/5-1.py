#coding:utf-8
#编写函数计算圆的面积
#import  math
from math import pi as PI
def area(x):
    if isinstance(x,int) or isinstance(x,float):
       return PI*x*x
    else:
        return ("you must give me an integer or float as redius.")
a=input("请输入圆的半径：")
print(area(int(a)))