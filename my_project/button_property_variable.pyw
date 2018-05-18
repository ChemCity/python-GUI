#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
#绑定Button与变量 
设置Button在textvariable属性 
"""
#import tkinter
from tkinter import *
root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()
#----------------------------------------------------------------------------
def chageText():
	if b['text'] == 'text':
		v.set('chage')
		print('change')
	else:
		v.set('text')
		print('text')
v = StringVar()
b = Button(root, textvariable=v, command=chageText)
v.set('text')
b.pack()
#-----------------------------------------------------------------------------
# 进入消息循环
root.mainloop()
