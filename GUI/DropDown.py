from tkinter import *


def doSomething():
    print("This will print only a msg")


def doSomethin():
    print("This will add only a project")


def doSomethe():
    print("This will open a project")


def doSomething1():
    print("This will exit ")


root = Tk()
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New Project', command=doSomethin)
filemenu.add_command(label='open Project', command=doSomethe)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=doSomething1)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=doSomething)
editmenu.add_command(label='copy', command=doSomething)

root.mainloop()
