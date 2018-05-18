#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import tkinter
from tkinter import *
import sys

import urllib.request

import urllib.parse
import json
import time
import random
import hashlib


root = Tk()

#设置窗口标题
root.title("翻译软件")
#设置窗口大小
root.geometry('300x200')

#设置窗口是否可以变化长宽
#宽不可以变 高可以变 默认为True
root.resizable(width = False, height = True)
def translate(content):
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.google.com/'
	data = {}

	u = 'fanyideskweb'
	d = content
	f = str(int(time.time()*1000) + random.randint(1,10))
	c = 'rY0D^0\'nM0}g5Mm1z%1G4'

	sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

	data['i'] = content
	data['from'] = 'AUTO'
	data['to'] = 'AUTO'
	data['smartresult'] = 'dict'
	data['client'] = 'fanyideskweb'
	data['salt'] = f
	data['sign'] = sign
	data['doctype'] = 'json'
	data['version'] = '2.1'
	data['keyfrom'] = 'fanyi.web'
	data['action'] = 'FY_BY_CL1CKBUTTON'
	data['typoResult'] = 'true'

	data = urllib.parse.urlencode(data).encode('utf-8')
	request = urllib.request.Request(url=url,data=data,method='POST')
	response = urllib.request.urlopen(request)
	html = response.read().decode('utf-8')
	#print(html)
	target = json.loads(html)  
	result = target['translateResult'][0][0]['tgt']
	return result
	
def printhello():
	var=t1.get('0.0', 'end')
	print(var)
	var = translate(var)
	t2.delete(0.0, END)
	t2.insert('1.0', var)
	t2.update()
	
def printEventInfo(event):
	printhello()
	print('event.time = ', event.time)  
	print('event.type = ', event.type)  
	print('event.WidgetId = ', event.widget)  
	print('event.KeySymbol = ', event.keysym)
	print('event.x = ',event.x, 'event.y = ', event.y)
	
t1 = Text(root, height=3, width=30)
t1.insert('1.0','我是谁')
t2 = Text(root, height=3, width=30)
t2.insert('1.0','t2')

btn = Button(root, text = "翻译", command = printhello)

root.bind("<Return>", printEventInfo)	#绑定事件 回车

btn.pack(side=BOTTOM, fill = X, padx=20,pady=10)
t1.pack(pady=20)
t2.pack(pady=10)


root.iconbitmap(sys.path[0] + '\\favicon.ico')  
# 进入消息循环
root.mainloop()
