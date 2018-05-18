# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    #req = request.Request("http://fanyi.baidu.com")
    #response = request.urlopen(req)
    response = request.urlopen("http://fanyi.baidu.com")
    #屏蔽的两行 和上面一行 获得的网页数据有何不同?
    html = response.read()
    html = html.decode("utf-8")
    print(html)
