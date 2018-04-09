#coding:utf-8
import requests
r = requests.get('http://quote.eastmoney.com/stocklist.html')
try:
    r.status_code
    r.encoding = r.apparent_encoding
    print r.text[:1000]
except:
    print '爬取失败'