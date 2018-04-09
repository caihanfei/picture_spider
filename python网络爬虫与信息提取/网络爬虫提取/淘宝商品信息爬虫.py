#coding:utf-8
#ajax异步，暂时无法爬取
import requests
import re

def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print r.text
    except:
        print '爬取失败'
    
def parsePage(ilt,html):
    print ""
    
def printGoodsList(ilt):
    print ""
    
def main():
    goods = "书包"
    depth = 2
    start_url = "https://s.taobao.com/search?q="+goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url+'&s'+str(44*i)
            html = getHtmlText(url)
            parsePage(infoList, html)
        except:
            continue
        printGoodsList(infoList)
            
getHtmlText('https://s.taobao.com/api?_ksTS=1521643628979_209&callback=jsonp210&ajax=true&m=customized&stats_click=search_radio_all:1&q=%E4%B9%A6%E5%8C%85&s=36&imgfile=&initiative_id=staobaoz_20180321&bcoffset=0&js=1&ie=utf8&rn=2acd749366b1426844b7c862ba9c227d?type=5&interval_id=100%3A90')