# https://mm.taobao.com/search_tstar_model.htm
# ajax:https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8
# 个人主页：https://mm.taobao.com/self/aiShow.htm?spm=719.7763510.1998643336.71.Yx0DbQ&userId=

import os
import requests
import re

url_ajax = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
url_base = 'https://mm.taobao.com/self/aiShow.htm?spm=719.7763510.1998643336.71.Yx0DbQ&userId='

params = {}
params['q'] = ''
params['viewFlag'] = 'A'
params['searchStyle'] = ''
params['searchRegion'] = 'city:'
params['searchFansNum'] = ''
params['currentPage'] = 2 # 页数
params['pageSize'] = 100

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'

resp = requests.get(url_ajax, params=params, headers=headers)

uni_str = resp.content.decode(resp.encoding) # unicode


pattern = re.compile('"city":"(.*?)".*?'
                     + '"height":"(.*?)".*?,'
                     + '"realName":"(.*?)".*?'
                     + '"userId":(.*?),')

# mm的个人信息
items = re.findall(pattern, uni_str)

base_dir = os.getcwd()

for item in items:
    city, height, name, id = item[0], item[1], item[2], item[3]
    if (os.path.exists(name) == False):
        os.mkdir(name)
    path = os.path.join(base_dir, name)

    url = url_base + id
    mm_page = requests.get(url)

    mm_str = mm_page.content.decode(resp.encoding)  # unicode

    mm_pattern = re.compile('img.*?src="(.*?)"')
    images = re.findall(mm_pattern, mm_str)

    num = 1

    for image in images:
        f_url = 'https:' + image.strip()
        if f_url[-3:].lower() != 'jpg' and f_url[-4:].lower() != 'jpeg':
            continue
        print(f_url)
        try:
            di = requests.get(f_url)
            f_path = os.path.join(path, str(num) + '.jpg')
            # 图片下载，单线程，很慢
            # 有些其他格式的图片也会变成jpg，可能无法打开
            with open(f_path, 'wb') as si:
                si.write(di.content)
                num += 1
        except:
            print('Failed:' + f_url)
