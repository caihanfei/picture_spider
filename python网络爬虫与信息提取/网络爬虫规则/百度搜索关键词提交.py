#encoding:utf-8
import requests
kv = {'wd':'Python'}
r = requests.get('http://www.baidu.com/s',params = kv)
try:
    print r.status_code
    print r.request.url
    print len(r.text)
    print r.content
except:
    print '爬取失败'