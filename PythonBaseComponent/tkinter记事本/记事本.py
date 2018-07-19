#coding:utf-8
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os
from email.policy import default
from setuptools.sandbox import save_argv
from asyncio.protocols import Protocol
filename = ''
def newfile():
    global filename
    root.title('未命名文件')
    filename = None
    textPad.delete(1.0, END)
# 保存和另存为
# 保存时保存在到一个默认的地址
# 另存是需要弹出一个对话框去存储你要存取的地址
def save():  # 封装保存
    global filename
    # 如果文件存在的话就是直接保存在默认的路径
    # 如果不存在的话就是另存为一个新的文件
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saves()
def saves():  # 文件的另存为保存
    f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')  # 初始化文件名和后缀名
    global filename
    filename = f
    fh = open(f, 'w')  # 打开文件写文件
    msg = textPad.get(1.0, END)  # 写入的内容得到
    fh.write(msg)  # 写入内容到文件
    fh.close()
    root.title('Filename:' + os.path.basename(f))  # 存储文件
def cut():
    textPad.event_generate('<<Cut>>')
def copy():
    textPad.event_generate('<<Copy>>')
def paste():
    textPad.event_generate('<<Paste>>')
def redo():
    textPad.event_generate('<<Redo>>')
def undo():
    textPad.event_generate('<<Undo>>')
def selectAll():
    textPad.tag_add('sel', '1.0', END)
root = Tk()
root.title('Simple text')
root.geometry('800x500+100+100')  # 构建一个矩形窗体    初始化的显示位置    100  100  大小  800x500
# 创建一个menu
menubar = Menu(root)
root.config(menu=menubar)
# 创建一系列的子menu
filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl + N', command=newfile)  # accelerator 快捷键，  new  点击事件函数
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + S', command=saves)
menubar.add_cascade(label='文件', menu=filemenu)

# 编辑菜单
editmenu = Menu(menubar)
editmenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + Y', command=redo)
editmenu.add_separator()  # 分隔符
editmenu.add_command(label='剪切', accelerator='Ctrl + X', command=cut)
editmenu.add_command(label='复制', accelerator='Ctrl + C', command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl + V', command=paste)
editmenu.add_separator()  # 分隔符
editmenu.add_command(label='全选',accelerator='Ctrl + A',command=selectAll)
menubar.add_cascade(label='编辑', menu=editmenu)
# linenumber&text
textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)  # 允许进行扩展 ,填充X，Y轴
scroll = Scrollbar(textPad)  # 右侧的移动下滑栏
textPad.config(yscrollcommand=scroll.set)  # 在Y轴显示   yscrollcommand
scroll.config(command=textPad.yview)  # 这是为了让编辑内容和下拉栏同时移动
scroll.pack(side=RIGHT, fill=Y)  # 显示

root.mainloop()