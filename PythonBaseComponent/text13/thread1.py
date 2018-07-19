#coding:utf-8
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import threading
import time
import queue
arg = 1
size = (int)(input())
myqueue = queue.Queue(size)
li = list()
for i in range(size):
    myqueue.put("hello"+str(i))
def count(self):
    for i in range(0,myqueue.qsize()):
        if myqueue.empty():
            break
        else:
            text.insert(END, myqueue.get() + '\n')
            time.sleep(0.1)
def func(self):
        th = threading.Thread(target=count, args=(arg,))
        th.setDaemon(True)
        th.start()
app = Tk()
app.title('threading')
app['width'] = 800
app['height'] = 600
text = ScrolledText(app, font=('隶书', 16), fg='black')
text.grid()
text.bind("<Button>",func)
app.mainloop()
