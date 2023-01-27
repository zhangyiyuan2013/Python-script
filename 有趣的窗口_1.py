import tkinter
from tkinter import Button

win=tkinter.Tk()
win.title('Login')
win.geometry('400x200')
t1=' Name: Zhang Yiyuan '
L1 = tkinter.Label(win, text=t1, bg='red')
L1.grid(row=0,column=0)
L2 = tkinter.Label(win, text=t1, bg='blue')
L2.grid(row=1,column=1)
L3 = tkinter.Label(win, text=t1, bg='green')
L3.grid(row=2,column=1)
L4 = tkinter.Label(win, text=t1, bg='yellow')
L4.grid(row=1,column=2)
win.mainloop()
