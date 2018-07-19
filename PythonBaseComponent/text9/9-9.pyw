import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext

#创建应用程序窗口
app = tkinter.Tk()
app.title('My Notepad----by Dong Fuguo')
app['width'] = 800
app['height'] = 600

textChanged = tkinter.IntVar()
textChanged.set(0)
#当前文件名
filename = ''




#将创建的菜单关联到应用程序窗口
app.config(menu=menu)

#创建文本编辑组件
txtContent = tkinter.scrolledtext.ScrolledText(app, wrap=tkinter.WORD)
txtContent.pack(fill=tkinter.BOTH, expand=tkinter.YES)
def KeyPress(event):
    textChanged.set(1)
txtContent.bind('<KeyPress>', KeyPress)

app.mainloop()
