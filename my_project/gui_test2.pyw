#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import tkinter
from tkinter import *
root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry('300x200')

#设置窗口是否可以变化长宽
#宽不可以变 高可以变 默认为True
root.resizable(width = False, height = True)

l = Label(root, text='show', bg='green',font=('Areal',12),width=5,height=2)
#l.pack(side=LEFT)   #这里的side可以赋值为LEFT RTGHT TOP BOTTOM
l.pack()
# 进入消息循环
root.mainloop()
