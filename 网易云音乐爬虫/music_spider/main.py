#coding:utf-8
from music_spider import html_down, html_output, html_url, html_parse
class spiderMain():
    def __init__(self):
        self.down = html_down.down()
        self.out = html_output.output()
        self.parsea = html_parse.parse()
        self.url_mange = html_url.mange()
    def craw(self,root_url):
        count = 1
        self.url_mange.add_new_url(root_url)
        while self.url_mange.has_url():
#             try:
                new_url = self.url_mange.get_url()
#                 print "craw %d : %s"%(count,new_url)
                new_html = self.down.get_html(new_url)
                new_urls,new_data = self.parsea.Parse(new_url,new_html)
                self.url_mange.add_new_urls(new_urls)
                self.out.collect(new_data)
                count+=1
                if(count == 500):
                        break;
            
#             except:
#                 print 'craw fail'
        self.out.file_output()
if __name__ == '__main__':
    
    root_url = 'http://music.163.com/#/discover/playlist/'
    mySpider = spiderMain()
    mySpider.craw(root_url)
   
