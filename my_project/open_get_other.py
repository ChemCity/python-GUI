# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com")
    response = request.urlopen(req)
    
    #geurl()返回的是一个url的字符串
    print("geturl打印信息:%s" %(response.geturl()))
    print("******************************************************")
    #info() 返回的是一些meta标记的元信息,包括一些服务器的信息
    print("info打印信息:%s" %(response.info()))
    print("******************************************************")
    #getcode()返回的是HTTP状态码,如果返回200表示请求成功.
    print("getcode打印信息:%s" %(response.getcode()))
    print("******************************************************")

