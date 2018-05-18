#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import tkinter
from tkinter import *
root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()
#FLAT:平
Button(root, text = "平", relief = FLAT).pack()
#GROOVE:凹槽
Button(root, text = "凹槽", relief = GROOVE).pack()
#凸起的
Button(root, text = "凸起的", relief = RAISED).pack()
#脊状
Button(root, text = "脊状", relief = RIDGE).pack()
#立体的
Button(root, text = "立体的", relief = SOLID).pack()
#凹陷的
Button(root, text = "凹陷的", relief = SUNKEN).pack()
# 进入消息循环
root.mainloop()
