import tkinter
import tkinter.messagebox
from tkinter import *
from userlogin.dbdao import DBConnect as log
from userlogin.control import regservice as r
class Login:
    def login(self):
        self.login1(self.username.get(),self.password.get())
    def login1(self,name,pwd):
        isLog=log.DBConnect(name,pwd)
        if isLog.isUser():
            self.setFlag(True)
            self.hide()
            root = Tk()
            app = r.Reg(root)
            root.mainloop()
        else:
            tkinter.messagebox.showerror('Python tkinter', message='Error')
    def cancel(self):
        self.username.set('')
        self.password.set('')
    def setFlag(self,flag):
        self.flag = flag
    def __init__(self,root):
        self.isHide = root
        self.flag = False
        self.username = StringVar()
        self.username.set('')

        self.password = StringVar()
        self.password.set('')

        self.label = Label(root, text = '用户名:')
        self.label.pack()

        self.entryName = Entry(root, textvariable=self.username)
        self.entryName.pack()

        self.label = Label(root, text='密码:')
        self.label.pack()

        self.entryPass = Entry(root, show='*', textvariable=self.password)
        self.entryPass.pack()
        button = Button(root)
        button['text'] = '登录'
        button['command'] = self.login
        button.pack()
        button1 = Button(root)
        button1['text'] = '重置'
        button1['command'] = self.cancel
        button1.pack()
        self.quit = Button(root, text="退出", command=root.quit)
        self.quit.pack()
    def hide(self):
        if self.flag:
            self.isHide.withdraw()




