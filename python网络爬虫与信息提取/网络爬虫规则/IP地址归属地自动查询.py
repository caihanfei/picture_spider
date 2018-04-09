#coding:utf-8
import requests
url = "http://www.ip138.com/ips1388.asp?ip="
r = requests.get(url+'202.204.80.112'+'&action=2')
r.encoding = r.apparent_encoding
print r.text
