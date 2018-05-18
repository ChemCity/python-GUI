#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
指定Button的宽度与高度 
width:    宽度 
height:    高度 
使用三种方式： 
1.创建Button对象时，指定宽度与高度 
2.使用属性width和height来指定宽度与高度 
3.使用configure方法来指定宽度与高度 
'''  
#import tkinter
from tkinter import *
root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()
#---------------------------------------------------------------------------
b1 = Button(root, text='30x1', width=30, height=2)
b1.pack()

b2 = Button(root, text='30x2')
b2['width'] = 30
b2['height'] = 3
b2.pack()

b3 = Button(root, text='30x3')
b3.configure(width=30, height=3)
b3.pack()
#---------------------------------------------------------------------------
# 进入消息循环
root.mainloop()
