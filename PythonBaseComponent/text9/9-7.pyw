import tkinter
import tkinter.messagebox
#用户登录界面
import pymysql
from text9.dbcon import *
#创建应用程序窗口
root = tkinter.Tk()
varName = tkinter.StringVar()
varName.set('')
varPwd = tkinter.StringVar()
varPwd.set('')
#创建标签
labelName = tkinter.Label(root, text='User Name:', justify=tkinter.RIGHT, width=80)
#将标签放到窗口上
labelName.place(x=10, y=5, width=80, height=20)
#创建文本框，同时设置关联的变量
entryName = tkinter.Entry(root, width=80,textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

labelPwd = tkinter.Label(root, text='User Pwd:', justify=tkinter.RIGHT, width=80)
labelPwd.place(x=10, y=30, width=80, height=20)
#创建密码文本框
entryPwd = tkinter.Entry(root, show='*',width=80, textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)
#登录按钮事件处理函数
def login():
    #获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    dbconn = DbConn("localhost", "root", "root", "school_db")
    cursor = dbconn.DBconnect()
    dbconn.Sql("select * from student limit 5")
    results = dbconn.result()
    i=0
    # liu 456
    # sun 123
    # li  789
    for row in results:
        stu_id = row[0]
        stu_name = row[1]
        stu_psd = row[2]
        print(row)
        if name == stu_name and pwd == stu_psd:
            tkinter.messagebox.showinfo(title='Python tkinter',message='OK')
            break
        else:
            i = i + 1
            continue
    print(i)
    if i>=len(results):
        tkinter.messagebox.showerror('Python tkinter', message='Error')
    dbconn.close()
#创建按钮组件，同时设置按钮事件处理函数
buttonOk = tkinter.Button(root, text='Login', command=login)
buttonOk.place(x=30, y=70, width=50, height=20)
#取消按钮的事件处理函数
def cancel():
    #清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')
buttonCancel = tkinter.Button(root, text='Cancel', command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)

#启动消息循环
root.mainloop()
