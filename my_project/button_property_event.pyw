#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
#button控件焦点问题
"""
#import tkinter
from tkinter import *

def cb1():
	print('button1 clicked')
	
def printEventInfo(event):
	print('event.time = ', event.time)  
	print('event.type = ', event.type)  
	print('event.WidgetId = ', event.widget)  
	print('event.KeySymbol = ', event.keysym)
	print('event.x = ',event.x, 'event.y = ', event.y)
def cb3():
	print("button3 clicked")
	
root = Tk()
#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()
 #---------------------------------------------------------------------------
b1 = Button(root, text="Button1", command=cb1)
b2 = Button(root, text="Button2")
#b2.bind("<Enter>", printEventInfo)		#鼠标移动到区域
b2.bind("<Button-1>", printEventInfo)	#绑定事件 左键单击
b3 = Button(root, text="Button3", command=cb3)

b1.pack()
b2.pack()
b3.pack()
 
#b2.focus_set()
 #---------------------------------------------------------------------------
# 进入消息循环
root.mainloop()


"""
事件				代码	
鼠标左键单击按下	1/Button-1/ButtonPress-1	 
鼠标左键单击松开	ButtonRelease-1	 
鼠标右键单击		3	 
鼠标左键双击		Double-1/Double-Button-1	 
鼠标右键双击		Double-3	 
鼠标滚轮单击		2	 
鼠标滚轮双击		Double-2	 
鼠标移动			B1-Motion	 
鼠标移动到区域		Enter	 
鼠标离开区域		Leave	 
获得键盘焦点		FocusIn	 
失去键盘焦点		FocusOut	 
键盘事件			Key	 
回车键				Return	 
控件尺寸变			Configure
"""
