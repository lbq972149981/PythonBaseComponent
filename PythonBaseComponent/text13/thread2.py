#coding:utf-8
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import threading
import time
import queue
import urllib3
import requests
li = list()
host = urllib3.get_host("http://localhost:8099/MeetingMag/web/MeetMag/menu.htm")
li.append("host:"+(str)(host))
status = requests.get("http://localhost:8099/MeetingMag/web/MeetMag/menu.htm").status_code
li.append("status:"+(str)(status))
charset = requests.get("http://localhost:8099/MeetingMag/web/MeetMag/menu.htm").encoding
li.append("charset:"+(str)(charset))
cookies = requests.get("http://localhost:8099/MeetingMag/web/MeetMag/menu.htm").cookies
li.append("cookies:"+(str)(cookies))
headers = requests.get("http://localhost:8099/MeetingMag/web/MeetMag/menu.htm").headers
li.append("headers:"+(str)(headers))
url = requests.get("http://localhost:8099/MeetingMag/web/MeetMag/menu.htm").url
li.append("url:"+(str)(url))
codes = requests.codes
li.append("codes:"+(str)(codes))
history = requests.get("http://localhost:8099/MeetingMag/web/MeetMag/menu.htm").history
li.append("history:"+(str)(history))
elapsed = requests.get("http://127.0.0.1:8099/").elapsed
li.append("elapsed:"+(str)(elapsed))
arg = 1
print(li)
myqueue = queue.Queue(len(li))

for v in li:
    myqueue.put(v)
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
