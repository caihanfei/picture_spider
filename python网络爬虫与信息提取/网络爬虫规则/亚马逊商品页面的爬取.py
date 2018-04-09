#coding:utf-8
import requests
head = {'user-agent':'Mozilla/5.0'}#模拟浏览器进行访问
r = requests.get('https://www.amazon.cn/gp/product/B01M8L5Z3Y',headers = head)
try:
    r.status_code
    print r.status_code
    r.encoding = 'utf-8'
#     print r.text
    print r.request.headers
    print r.encoding
except:
    print ('爬取失败')
    
