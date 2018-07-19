
#-*-coding:utf-8-*-
s=0
for i in range(1,101):#返回一个range对象，不包括终值
    s=s+i
print('1+2+3+...+100=',s)
print('1+2+3+...+100=',sum(range(1,101)))#直接使用内置函数来实现题目的要求
