import urllib2



class down(object):
    def get_html(self,url):
        if url is None:
            return None
        headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }
        request = urllib2.Request(url,None,headers)
        
        response = urllib2.urlopen(request,timeout=60)
        
        if response.getcode() != 200:
            return None
        
        return response.read()