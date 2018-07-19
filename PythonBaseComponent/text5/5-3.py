#coding:utf-8
#编写函数，接收字符串参数，返回一个元祖，其中第一个元素为大写字母个数
#第二个元素为小写字母个数
def demo(s):
    sum=0
    sum1=0
    for i in s:
        if'a'<=i<='z':
          sum=sum+1
        else:
          'A'<=i<='Z'
          sum1=sum1+1
    print('大写字母个数为：',sum1)
    print('小写字母个数为：',sum)
demo('aabbHFJDK')
