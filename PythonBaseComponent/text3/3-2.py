#整数求和
endFlag='yes'#定义一个字符串
s=0
while endFlag.lower()=='yes':#lower()副本，用于将大小写字母转换成为小写字母
    x=int(input("请输入一个正整数："))#接收键盘输入的内容
    #x=eval(x)
    if isinstance(x,int) and 0<=x<=100:#isinstance（）测试对象是否属于指定类型的实例
        s=s+x
    else:
        print('不是数字或不符合要求')
        endFlag=input('继续输入？(yes or no)')#再次接收键盘输入内容
    print('整数之和=', s)