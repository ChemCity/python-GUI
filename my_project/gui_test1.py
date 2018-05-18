#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
root = Tk()     #创建窗口对象的背景色

#创建两个列表
li      = ['c','python','php','html','SQL','java']
movie   = ['CSS','jQuery','Bootstrap']
listb   = Listbox(root)     #创建两个列表组建
listb2  = Listbox(root)

#第一个小部件插入数据
for item in li:             #
    listb.insert(0,item)

#第二个小部件插入数据
for item in movie:
    listb2.insert(0, item)

#将小部件防止到主窗口中
listb.pack()

listb2.pack()

#进入消息循环
root.mainloop()
