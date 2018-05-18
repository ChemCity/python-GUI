# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
        # html = responese.read()
    except error.HTTPError as e:
        print(e.code)

#最后值得注意的一点是，如果想用HTTPError和URLError一起捕获异常，
##那么需要将HTTPError放在URLError的前面，
#因为HTTPError是URLError的一个子类。如果URLError放在前面，
#出现HTTP异常会先响应URLError，这样HTTPError就捕获不到错误信息了
