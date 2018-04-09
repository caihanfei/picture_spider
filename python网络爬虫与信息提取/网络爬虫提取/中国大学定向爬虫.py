#coding:utf-8
import requests
from bs4 import BeautifulSoup
import bs4
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class spider(object):
    def getHtml(self,url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print "fail"
    def fillUnivList(self,ulist,html):
        soup = BeautifulSoup(html,'html.parser')
        for tr in soup.find('tbody').children:
            if isinstance(tr,bs4.element.Tag):
                tds = tr('td')
                ulist.append([tds[0].string,tds[1].string.encode('utf-8'),tds[2].string.encode('utf-8')])
     
    def printUnivList(self,ulist,num):
        print ('{:<1}\t{:<20}\t{:<15}\t').format('排名','学校名称','地点')
#         print '\n'
        for i in range(num):
            u = ulist[i]
            print ('{:<1}\t{:<20}\t{:<15}\t'.format(u[0],u[1],u[2]))
        print ('Suc'+str(num))
        
        with open("output.html",'w') as fout:  
            fout.write("<html>")
            fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
            fout.write("<body>")
            fout.write("<table border = ‘1’>")
            fout.write("<tr>")
            fout.write("<td>排名</td>")
            fout.write("<td>学习名称</td>")
            fout.write("<td>地点</td>")
            fout.write("</tr>")
            for i in range(num):
                u = ulist[i]
                fout.write("<tr>")
                fout.write("<td>%s</td>"%u[0])
                fout.write("<td>%s</td>" %u[1])
                fout.write("<td>%s</td>" %u[2])
                fout.write("</tr>")
            
            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")
if __name__=='__main__':
    sp = spider()
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = sp.getHtml(url)
    sp.fillUnivList(uinfo, html)
    sp.printUnivList(uinfo,500)
    