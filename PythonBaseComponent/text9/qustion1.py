import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext
import threading
import queue
class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
    def run(self):
        global myqueue
        myqueue.put(self.getName())

class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
    def run(self):
        global myqueue

myqueue = queue.Queue()
li = ["hh","aa","dd"]
def shows():
    for i in range(10):
        for v in li:
            p = Producer(v)
            li.remove(v)
            print(p)
#创建应用程序窗口
app = tkinter.Tk()
app.title('threading')
app['width'] = 800
app['height'] = 600
textChanged = tkinter.IntVar()
textChanged.set(0)
#创建文本编辑组件
txtContent = tkinter.scrolledtext.ScrolledText(app, wrap=tkinter.WORD)
txtContent.pack(fill=tkinter.BOTH, expand=tkinter.YES)
txtContent.bind('<show>', shows())
app.mainloop()
