#conding:utf-8
from photoSpider import url_manger, html_parse, html_output
from photoSpider import html_dwon


class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manger.UrlManger()
        self.downloader = html_dwon.HtmlDownloader()
        self.parser = html_parse.HtmlParser()
        self.outputer = html_output.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                        
                print "craw %d : %s"%(count, new_url)
            
                html_cont = self.downloader.Download(new_url)
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                        
                if(count == 1000):
                    break;
                    
                count = count + 1 
            except:
                print "craw failed"
             
        self.outputer.downAllphoto()
            
            
        


if __name__=='__main__':
    root_url = 'http://www.mmonly.cc/tag/cs/'
    spider_start = SpiderMain()
    spider_start.craw(root_url)