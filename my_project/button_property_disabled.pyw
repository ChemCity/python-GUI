#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
#button单击禁用 在单击恢复
"""
#import tkinter
from tkinter import *
root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()
#----------------------------------------------------------------------------
def setstate(event):
	if(btn['state'] != DISABLED):
		btn['state'] = DISABLED
		btn['text'] = '失效'
	else:
		btn['state'] = NORMAL
		btn['text'] = '正常'
btn = Button(root, text='正常', state='normal', width=20)
btn.bind("<Button-1>", setstate)
btn.pack(side=LEFT)
#-----------------------------------------------------------------------------
# 进入消息循环
root.mainloop()
