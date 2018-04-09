# coding:utf-8
import requests

# requests.request()构造一个请求，支撑以下各种方法的基础方法
# 
# requests.get()获取html网页的主要方法，对应于http的get
# requests.head()获取html网页头信息的方法，对应于http的head
# requests.post()向html网页提交post请求的方法，对应于http的post
# requests.put()向html网页提交put请求的方法，对应于http的put
# requests.patch()向html网页提交局部修改请求，对应http的patch
# requests.delete()向html页面提交删除请求，对应http的delete


r = requests.head('http://www.baidu.com')
print r.headers#头信息


info = {'penglu':19,'caihanfei':'19'}
i = requests.post('http://www.baidu.com',data = info)#提交信息
# print i.text


res = requests.get('http://www.baidu.com')
print res.status_code#状态码 200为成功 404为失败
print res.headers#得到头信息
print res.text#url页面内容
print res.encoding#从http header猜测的响应内容编码方式
print res.content#http 响应内容二进制
res.raise_for_status()#如果状态不是200，直接抛出异常



print res.apparent_encoding#从内容中分析出的响应内容编码方式
res.encoding = 'utf-8'
print res.text

rea = requests.request('GET', 'http://baidu.com',params = info)
print rea.url
