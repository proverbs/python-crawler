# -*- coding:utf-8 -*-

import requests
import json

url = 'http://httpbin.org'

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
files = {'file': open('cookie.txt', 'rb')}
cookies = {'cookies_are': 'working'}

proxies = {
    'http': 'http://183.128.180.240:808',
    'https': 'http://101.23.150.109:9999'
}
s = requests.Session()
res = s.get('http://httpbin.org/get', proxies=proxies)
print(res.text)



'''
print(type(res))
print(res.status_code)
print(res.encoding)
print(res.cookies)
'''
