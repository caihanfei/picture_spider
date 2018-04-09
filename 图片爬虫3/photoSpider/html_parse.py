from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    def get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/mmtp/'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def get_new_photo(self,soup):
        imglist = set()
        imgs = soup.find_all('img',src=re.compile(r'/uploads/'))
        for img in imgs:
            tupian = img['src']
            imglist.add(tupian)
        return imglist
    

    def parse(self,url,html):
        if url is None or html is None:
            return None
        soup = BeautifulSoup(html,'html.parser',from_encoding = 'utf-8')
        urls = self.get_new_urls(url,soup)
        photos = self.get_new_photo(soup)
        return urls,photos


