import urllib.request

import urllib.parse
import json
import time
import random
import hashlib

while 1:
    content = input('请输入需要翻译的句子：')
    
    if (content == 'q'):
        print('退出')
        break
    
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
    print (result) 

