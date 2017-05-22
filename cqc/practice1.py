# -*- coding:utf-8 -*-
# 功能：爬取糗事百科的段子
# to-do:完善交互

from urllib import request, parse, error
import re

page = 2
url = 'http://www.qiushibaike.com/text/page/' + str(page)

try:
    values = {}
    values['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
    values['Referer'] = 'http://www.qiushibaike.com/hot/'
    req = request.Request(url, headers=values)
    res = request.urlopen(req)

    text = res.read().decode('utf-8')
    pattern = re.compile('<div class="author clearfix">.*?'
                         + '<h2>(.*?)</h2>.*?'
                         + '<div class="content">.*?'
                         + '<span>(.*?)</span>.*?'
                         + '</div>', re.S)

    items = re.findall(pattern, text)

    br = '<br.?>'
    for i in range(len(items)):
        print('用户：' + items[i][0])
        print('段子: ' + re.sub(br, '\n', items[i][1]) + '\n\n')# 将br转换为换行

except error.URLError as e:
    print(e.reason)