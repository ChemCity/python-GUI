#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import tkinter
from tkinter import *
root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()

def printhello():
    t.insert('1.0', "hello\n")

t = Text()
t.pack()
Button(root, text = "press", command = printhello).pack()

# 进入消息循环
root.mainloop()
