import tkinter
from tkinter import Button

win=tkinter.Tk()
win.title('4399小游戏登录界面/第三方登录(推荐)')
win.geometry('400x400')
L1 = tkinter.Label(win, text='4399账号注册',font='Helvetica  -36 bold' )
L1.grid(row=0,column=2)
L2 = tkinter.Label(win, text='4399用户名*：', font='song -20')
L2.grid(row=1,column=1)
L3 = tkinter.Label(win, text='密码*：', font='song -20')
L3.grid(row=2,column=1)
L4 = tkinter.Label(win, text='邮箱：', font='song -20')
L4.grid(row=3,column=1)

e1=tkinter.Entry(win,width=20,font='song -20')
e2=tkinter.Entry(win,width=20,font='song -20')
e3=tkinter.Entry(win,width=20,font='song -20')
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)
def mClick():
    L5 = tkinter.Label(win, text='注册成功！', bg='red')
    L5.grid(row=6,column=2)

btn=tkinter.Button(win,text='注册',bg='white',command=mClick)
btn.grid(row=5,column=2)
win.mainloop()

