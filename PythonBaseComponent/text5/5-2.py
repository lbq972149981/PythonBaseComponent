#coding:utf-8
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

