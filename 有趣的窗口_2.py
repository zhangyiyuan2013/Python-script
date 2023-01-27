import tkinter as tk
window = tk.Tk()
window.title("佐佑思维")
#-------------------------------------------------------------
#label标签框的设置
l_00 = tk.Label(window, text="请关注“佐佑思维”并输入你的需求到后台询问", font=("微软雅黑", 12))
l_00.pack(pady=10)

#设置输入框
e_00 = tk.Entry(window, font=("微软雅黑", 20))
e_00.pack()

def get():    
    print('这里定义一个函数来作为点击开始按钮的响应')
           
b1 = tk.Button(window, text="开始", command=get)
b1.pack(pady=10) #设置布局上的代码

#设置清空按钮
def ok():
    e_00.delete(0, "end")

b2 = tk.Button(window, text="清空", command=ok)
b2.pack(before=b1,side='left',padx=70,pady=10)

import os
from tkinter import messagebox

#关闭按钮的设置：以下的设置会让你点击关闭按钮[X]后完全中断并退出Python所有进程
def callbackClose():
    messagebox.showwarning(title='警告', message='可爱的你点击了 [关闭] 按钮')
    os._exit(0)

window.protocol("WM_DELETE_WINDOW", callbackClose) #protocol的使用：控件.protocol(protocol，handler)，其中控件为窗口对象(Tk,Toplevel)
                                                   #常见protocol有： WM_DELETE_WINDOW：最常用的协议称为WM_DELETE_WINDOW，用于定义用户使用窗口管理器明确关闭窗口时发生的情况。如果使用自己的handler来处理事件的话，这时候窗口将不会自动执行关闭
                                                   #WM_TAKE_FOCUS，WM_SAVE_YOURSELF：[这两个不知道什么来的。]

window.mainloop() # 进入消息循环
