#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import tkinter
from tkinter import *
import socket
import time
HOST = "192.168.1.5"
PORT = 8888

root = Tk()

#设置窗口标题
root.title("hello world")
#设置窗口大小
root.geometry()

def printhello():
   
    try:
        
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)
    #t.insert('1.0', "hello\n")
    try:
        s.connect((HOST,PORT))       #要连接的IP与端口
    except socket.error as e:
        print("Error connect socket: %s" % e)
        sys.exit(1)
   # t.insert('1.0', "hello2\n")
    st = "hello\r\n"
    try:
        
        s.send(st.encode())      #把命令发送给对端
    except socket.error as e:
        print("Error sendall socket: %s" % e)
        sys.exit(1)
    #t.insert('1.0', "hello3\n")
    time.sleep(0.1)
    #data=s.recv(1024)     #把接收的数据定义为变量
    #t.insert("1.0", data)
    s.close()
t = Text()
t.pack()
Button(root, text = "press", command = printhello).pack()

# 进入消息循环
root.mainloop()
