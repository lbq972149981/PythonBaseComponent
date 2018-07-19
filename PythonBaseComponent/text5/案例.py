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

#编写函数，接受任意多个实数，返回一个元祖，其中第一个元素为所有参数的平均值
#其他元素为所有参数中大于平均值的实数
def demo(*p):  #方法1
     a=len(p)
     sum=0
     r=[]
     for i in p:
         sum=sum+i
     a=sum/a
     for x in p:
         if x>a:
           r.append(x)
     print(a)
     print(list(r))
demo(1,2,3,4)

def demo(*para):
    avg=sum(para)/len(para)
    g=[i for i in para if i>avg]  #*******
    return (avg,)+tuple(g)
print(demo(1,2,3,4))


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

#5-4
def demo(lis,k):
   x=lis[:k]
   x.reverse()
   y=lis[k:]
   y.reverse()
   r=x+y
   r.reverse()
   print(x)
   print(y)
   print(r)
lit=(list(range(1,21)))
print(lit)
demo(lit,9)

#5-5
def demo(t):
    a,b=1,1
    while b<t:
        a,b=b,a+b
    else:
        return b
print(demo(50))

#5-6
import random
def demo(lst):
    m=min(lst)
    result = (m,)
    for index ,value in enumerate(lst):
        if value==m:
            result = result+(index,)
    return result
x=[random.randint(1,20) for i in range(10)]
print(x)
print(demo(x))

#5-7
def demo(t):
    print([1])
    print([1,1])
    line=[1,1]
    for i in range(2,t):
        r=[]
        for j in range(0,len(line)-1):
           r.append(line[j]+line[j+1])
        line=[1]+r+[1]
        print(line)
demo(10)

#5-8
import math
def IsPrime(n):
    m=int(math.sqrt(n))+1
    for i in range(2,m):
        if n%i==0:
            return  False
    return  True

def demo(n):
    if isinstance(n,int)and n>0and n%2==0:
        for i in range(3,int(n/2)+1):
            if i%2==1 and IsPrime(i) and IsPrime(n-i):
                print(i,'+',n-i,'=',n)
demo(60)

#5-9
def demo(m,n):
    if m>n:
        m,n=n,m
    p=m*n
    while m!=0:
        r=n%m
        n=m
        m=r
    return (int(p/n),n)
print(demo(20,30))

#5-10
import random
def demo(x,n):
    if n not in x :
        print(n,'is not an element of ',x)
        return
    i=x.index(n)
    x[0],x[i]=x[i],x[0]
    key=x[0]

    i=0
    j=len(x)-1
    while i<j:
        while i<j and x[j]>=key:
            j-=1
            x[i]=x[j]

        while i<j and x[i]<=key:
            i+=1
        x[j]=x[i]
        x[i]=key
x=list(range(1,10))
random.shuffle(x)
print(x)
demo(x,4)
print(x)

#5-11
def Rate(origin,userInput):
    if not (isinstance(origin,str) and isinstance(userInput,str)):
        print('The teo parameters must be strings.')
        return
    if len(origin)<len(userInput):
        print('Sorry.I suppose the seond parmeter string is shorter.')
        return
    right=0
    for origin_char,user_char in zip(origin,userInput):
        if origin_char==user_char:
            right+=1
    return right/len(origin)
origin='Shandong Institute of Business and Technology'
uesrInput='Shandong institute of business and technology'
print(Rate(origin,uesrInput))