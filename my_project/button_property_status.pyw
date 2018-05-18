#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''''
设置button的边框 风格 状态 
'''   
#import tkinter
from tkinter import *
root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()
#---------------------------------------------------------------------------
#设置button的前景色与背景色
#fg:前景色  bg:背景色

bfg = Button(root, text='change foreground', fg='red')
bfg.pack()

bbg = Button(root, text='change background', bg='blue')
bbg.pack()

hello_bt = Button(root, text='hello button', fg='red', bg='blue')
hello_bt.pack()


#设置button的边框
#bd(bordwidth:缺省为1或2个像素)
#创建5个Button边框宽度依次为:0,2,4,6,8
for b in [0,1,2,3,4]:
	Button(root, text=str(b), bd=b).pack()

#设置Button的风格
#relief/raised/sunken/groove/redge
for r in ['raised', 'sunken', 'groove', 'ridge']:
	Button(root, text = r, relief = r, width = 30).pack()
	
#设置Button状态
#normal/active/disabled
def statePrint():
		print('state')
for r in ['normal', 'active', 'disabled']:
	Button(root, text=r,state=r,width=30,command=statePrint).pack()


#---------------------------------------------------------------------------
# 进入消息循环
root.mainloop()
