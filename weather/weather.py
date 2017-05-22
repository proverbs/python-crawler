# http://www.weather.com.cn/weather/101280101.shtml
# 从以上网址爬取广州天气

import requests
import re
from bs4 import BeautifulSoup

url_gz = 'http://www.weather.com.cn/weather/101280101.shtml'

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'

resq = requests.get(url_gz, headers=headers)
resq.encoding = 'utf-8' # requests获取的编码有可能是错误的，需要手工指定

soup = BeautifulSoup(resq.text, 'lxml')

title = soup.head.title
print(title.string)

body = soup.body
info = body.find('ul', class_='t clearfix')

info_list = info.find_all('li')
pattern = re.compile('<h1>(.*?)</h1>.*?'
                     + '<p title=".*?" class="wea">(.*?)</p>.*?'
                     + '<i>(.*?)</i>.*?'
                     + '<i>(.*?)</i>')
for day in info_list:
    #print(type(day))
    #print(day, '\n')
    wea = day.find('p', class_='wea')
    tem = day.find('p', class_='tem')
    win = day.find('p', class_='win')
    print(day.h1.string, wea.string, tem.i.string, win.i.string)
    #items = re.findall(pattern, day)
    #for item in items:
    #    print(item[0], item[1], item[2], item[3])


