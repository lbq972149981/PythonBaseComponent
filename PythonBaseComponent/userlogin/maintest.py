from tkinter import Tk

from userlogin.control.loginservice import Login

if __name__ == '__main__':
    root = Tk()
    root.title("用户登录")
    app = Login(root)
    root.mainloop()