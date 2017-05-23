'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 模拟百度搜索

driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')

assert "百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(driver.page_source)
'''

# 利用selenium模拟登录考研论坛

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url_yd = 'https://note.youdao.com/signIn/index.html?&callback=http%3A%2F%2Fnote.youdao.com%2Foldweb' # 旧版界面
url_ky = 'https://i.kaoyan.com/login?url=http://bbs.kaoyan.com/forum.php'

driver = webdriver.Firefox()
driver.get(url_ky)

assert '考研' in driver.title

elem_usr = driver.find_element_by_name('uname')
elem_pas = driver.find_element_by_name('passwd')
elem_code = driver.find_element_by_name('seccode')

elem_usr.send_keys('379548839@qq.com')
elem_pas.send_keys('xxxxxx') # 保密
# elem_code.screenshot('code.png')

x = input() # 等待手工输入验证码
# 由于验证码有bug，必须多次刷新才能使用，必须手工输入
print('验证码为：', x)
elem_pas.send_keys(Keys.RETURN)


cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
cookiestr = ';'.join(item for item in cookie)

print(cookiestr)



import requests

url_hm = 'https://i.kaoyan.com/set/profile'
headers = {}
headers['Host'] = 'i.kaoyan.com'
headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
headers['cookie'] = cookiestr
headers['Referer'] = 'http://bbs.kaoyan.com/forum.php'

resp = requests.get(url_hm, headers=headers)

print(resp.text)
