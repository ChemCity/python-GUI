#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
#button显示图像和文本
"""
#import tkinter
from tkinter import *
root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()
#图像居下,居上,居右,居左,文字位于图像之上
Button(root, text = 'botton', compound = 'bottom', bitmap = 'error').pack()
Button(root, text='top', compound='top', bitmap='error').pack()  
Button(root, text='right', compound='right', bitmap='error').pack()  
Button(root, text='left', compound='left', bitmap='error').pack()  
Button(root, text='center', compound='center', bitmap='error').pack() 
# 进入消息循环
root.mainloop()
