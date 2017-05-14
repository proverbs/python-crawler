from urllib import request, error, parse
from http import cookiejar

file_name = 'cookie.txt'
# 使用firefox的tamperdata插件获取post地址，注意还要补充header
url = 'http://222.200.182.10/docs/studentLogin.php?db=CompilersOnline'

values = {'username': 'xxxxxx', 'password': '*****'} # 填写账号、密码
values['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
values['Referer'] = 'http://222.200.182.10/compilersindex.htm'

data = parse.urlencode(values)
b_data = data.encode('utf8')

cookie = cookiejar.MozillaCookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)

response = opener.open(url, b_data)
print(response.read())

cookie.save(file_name, ignore_discard=True, ignore_expires=True)

# 利用有cookie的opener访问个人信息页
t_url = 'http://222.200.182.10/docs/showSelfInformation.php'
res = opener.open(t_url)

print(res.read())
