import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from text9.dbcon import *
class Reg:
    def __init__(self,root):
        self.varName = StringVar()
        self.varName.set('')
        self.labelName=Label(root, text='Name:',justify=tkinter.RIGHT)
        self.labelName.pack()
        self.entryName=Entry(root, textvariable=self.varName)
        self.entryName.pack()
        self.labelGrade=Label(root, text='Grade:', justify=tkinter.RIGHT)
        self.labelGrade.pack()
        self.studentClasses = {'1': ['1', '2', '3', '4'],
                          '2': ['1', '2'],
                          '3': ['1', '2', '3']}
        self.comboGrade=ttk.Combobox(root,
                     values=tuple(self.studentClasses.keys()))
        self.comboGrade.bind('<<ComboboxSelected>>', self.comboChange)
        self.comboGrade.pack()
        self.labelClass=Label(root, text='Class:', justify=tkinter.RIGHT)
        self.labelClass.pack()
        self.comboClass = ttk.Combobox(root)
        self.comboClass.pack()
        self.labelSex = tkinter.Label(root, text='Sex:', justify=tkinter.RIGHT)
        self.labelSex.pack()

        self.sex = IntVar()
        self.sex.set(1)

        self.radioMan = Radiobutton(root, variable=self.sex, value=1, text='Man')
        self.radioMan.pack()
        self.radioWoman = Radiobutton(root,variable=self.sex,value=0,text='Woman')
        self.radioWoman.pack()
        self.monitor = IntVar()
        self.monitor.set(0)
        self.checkMonitor = Checkbutton(root, text='Is Monitor?', variable=self.monitor,
                                           onvalue=1, offvalue=0)
        self.checkMonitor.pack()
        self.buttonAdd = Button(root, text='添加',  command=self.addInformation)
        self.buttonAdd.pack()
        self.buttonDelete = Button(root, text='删除',
                                      command=self.deleteSelection)
        self.buttonDelete.pack()
        self.listboxStudents = Listbox(root, width=50)
        self.listboxStudents.pack()

        self.quit =  Button(root, text="退出", command=root.quit)

        self.quit.pack()

    def addInformation(self):
        dbconn = DbConn("localhost", "root", "root", "school_db")
        cursor = dbconn.DBconnect()
        Name = self.entryName.get()
        Grade = self.comboGrade.get()
        Class = self.comboClass.get()
        Sex = ('Man' if self.sex.get() else 'Woman')
        Monitor = ('Yes' if self.monitor.get() else 'No')
        sql = "insert into student1 VALUES('%s','%s','%s')" % (Name, Grade, Class)
        dbconn.Sql(sql)
        dbconn.commit()
        dbconn.close()
        result ="姓名：",Name,"班级：",Grade,"年级：",Class,"性别：",Sex,"是否为班长：",Monitor
        self.listboxStudents.insert(0, result)

    def comboChange(self,event):
        grade = self.comboGrade.get()
        if grade:
            # 动态改变组合框可选项
            self.comboClass["values"] = self.studentClasses.get(grade)
        else:
            self.comboClass.set([])

    def deleteSelection(self):
        selection = self.listboxStudents.curselection()
        if not selection:
            tkinter.messagebox.showinfo(title='Information', message='No Selection')
        else:
            self.listboxStudents.delete(selection)



