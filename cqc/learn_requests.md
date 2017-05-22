# requests模块学习

## 基础

### 基本请求

- `requests`支持http的6种基本请求（get，post，put，delete，head，options），请求名即为函数名
- `get`方法：`res = requests.get(url)`，返回的是`Response`实例，主要包含如下属性
  - `res.status_code`
  - `res.url`
  - `res.encoding`
  - `res.cookies`：如果`response`中包含cookie，则可通过`cookies`属性获取
  - `res.text`
  - `res.content`


### get

- `get`添加参数：

```python
payload = {'key1': 'value1', 'key2': 'value2'}
res = requests.get("http://httpbin.org/get", params=payload)
print(res.url) # http://httpbin.org/get?key2=value2&key1=value1
```

- `get`添加headers：

```python
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
res = requests.get("http://httpbin.org/get", params=payload, headers=headers)
print(res.text)
'''
{
  "args": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"
  }, 
  "origin": "120.236.174.143", 
  "url": "http://httpbin.org/get?key2=value2&key1=value1"
}
'''
```

### post

- `post`请求：表单格式，数据时存储在`form`域中的

```python
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
res = requests.post("http://httpbin.org/post", data=payload)
print(res.text)
'''
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
	"key1": "value1", 
	"key2": "value2"
  }, 
  "headers": {
	"Accept": "*/*", 
	"Accept-Encoding": "gzip, deflate", 
	"Connection": "close", 
	"Content-Length": "23", 
	"Content-Type": "application/x-www-form-urlencoded", 
	"Host": "httpbin.org", 
	"User-Agent": "python-requests/2.9.1"
  }, 
  "json": null, 
  "origin": "120.236.174.143", 
  "url": "http://httpbin.org/post"
}
'''
```

- `post`请求：json格式，数据时存储在`data`域和`json`域中的

```python
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
res = requests.post("http://httpbin.org/post", data=json.dumps(payload))
print(res.text)
'''
{
  "args": {}, 
  "data": "{\"key1\": \"value1\", \"key2\": \"value2\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "36", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.9.1"
  }, 
  "json": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "origin": "120.236.174.143", 
  "url": "http://httpbin.org/post"
}
'''
```

- `post`上传文件

```python
files = {'file': open('cookie.txt', 'rb')}
res = requests.post("http://httpbin.org/post", files=files)
print(res.text)
'''
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "# Netscape HTTP Cookie File\n# http://curl.haxx.se/rfc/cookie_spec.html\n# This is a generated file!  Do not edit.\n\n222.200.182.10\tFALSE\t/\tFALSE\t\tPHPSESSID\ta3p2qqe0fq4ct59ajdatdtdsd2\n"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "327", 
    "Content-Type": "multipart/form-data; boundary=5f160535f3d44a8ca29a65bee7cd33fb", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.9.1"
  }, 
  "json": null, 
  "origin": "120.236.174.143", 
  "url": "http://httpbin.org/post"
}
'''
```

### cookie

- 带`cookie`的`get`请求

```python
cookies = {'cookies_are': 'working'}
res = requests.get("http://httpbin.org/cookies", cookies=cookies)
print(res.text)
'''
{
  "cookies": {
    "cookies_are": "working"
  }
}
'''
```

- 超时配置：`requests.get('https://github.com', timeout=0.01)`，其中`timeout`只对请求时间有效，对下载时间无效

## 高级

### 会话Session

- 会话`session`：直接使用`get`之类的每个请求都相当于用不同浏览器发出的请求，是独立的；普遍地，网站登陆后，在同一个网站的不同网页中切换时，cookie是不变的，也就是一个持久的会话

- `session`实践：

  其中，res1这个Respone已经包含了网站返回的cookie，此时，s中就也已经包含了cookie。所以，res2对应的get请求也包含了cookie。

```python
s = requests.Session()
res1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
res2 = s.get('http://httpbin.org/cookies')
print(res1.text)
print(res2.text)
```

- `session`的`headers`配置：
  - 全局配置：`s.headers.update({'x-test': 'true'})`
  - 局部配置（可覆盖全局配置）：`res = s.get('http://httpbin.org/headers', headers={'x-test1': 'false'})`

### SSL证书验证

- https 开头的网站，requests可以为HTTPS请求验证网站的SSL证书
- 实践：
  - `res = requests.get('https://kyfw.12306.cn/otn/', verify=True)`
  - 12306证书是无效的，会抛出异常`requests.exceptions.SSLError`

### 代理

- 可以按照不同的协议设置不同的代理
- 实践：

```python
proxies = {
    'http': 'http://183.128.180.240:808',
    'https': 'http://101.23.150.109:9999'
}
s = requests.Session()
res = s.get('http://httpbin.org/get', proxies=proxies)
print(res.text)
'''
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.9.1"
  }, 
  "origin": "183.128.180.240", 
  "url": "http://httpbin.org/get"
}
'''
```

