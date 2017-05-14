# python爬虫 整理

## urllib

### urllib.request

#### urllib.request.urlopen

- 原型：`request.urlopen(url, data, timeout)`
- 返回：Request类实例
- 实践：`response = request.urlopen('http://blog.proverbs.top')`

#### urllib.request.read

- 返回：Request实例的文本
- 实践：`request.read()`

#### urllib.request.Request

- 推荐使用构建`Request`实例作为`urlopen`的参数
- 构建：`req = request.Request('http://blog.proverbs.top')`
- 实践：`res = request.urlopen(req)`

#### urllib.request.ProxyHandler

- `urllib`默认使用环境变量`http_proxy`作为代理
- 手动设置代理：使用`Handler`可以构建`opener`，而`opener`代替`urlopen`

```python
proxy_handler = request.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
opener = request.build_opener(proxy_handler)
request.install_opener(opener)
```

#### opener

- `urlopen`是特殊的一种`opener`，可以理解为`opener`的一个实例
- `http.cookiejar`可提供存储cookie的对象，其中：CookieJar —-派生—->FileCookieJar —-派生—–>MozillaCookieJar和LWPCookieJar
- 示例：

```python
from urllib import request, error
from http import cookiejar

#声明一个CookieJar对象实例来保存cookie
cookie = cookiejar.MozillaCookieJar()
#利用request库的HTTPCookieProcessor对象来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = request.build_opener(handler)
#此处的open方法同request的urlopen方法，也可以传入Request
response = opener.open('https://www.baidu.com')
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)
# cookie保存到文件，使用load可将cookie加载，参数与save相同
cookie.save('cookie.txt', ignore_discard=True, ignore_expires=True)
```

- 实践：模拟登录sysu在线课程系统

```python
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
```



### urllib.parse

#### urllib.parse.urlencode

- 用于通过`dict`构造`urlopen`中的`data`域，实现`POST`方法
- 实践：

```python
values = {"username":"379548839@qq.com","password":"password"}
data = parse.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
```

- `GET`方法：很POST方法一样，唯一不同的是网址需要带参数的url

### urllib.error

#### urllib.error.URLError

- 产生原因：无法联网；无法连接服务器
- 实践：

```python
req = request.Request('http://www.provb.top')
try:
    request.urlopen(req)
except error.URLError as e:
    print('fuck:', e.reason)
```



## Web

### Headers

- 浏览器访问网页是发送请求会包含`headers`
- `User-Agent`表示请求设备描述，`Referer`表示从请求来源（防盗链）
- `Header`是需要加入`data`中构造的

### cookies

- Cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）



## 正则表达式

[cqc的博客](http://cuiqingcai.com/977.html)

