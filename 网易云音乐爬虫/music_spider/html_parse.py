import urlparse
import re
from bs4 import BeautifulSoup
class parse(object):
    def _get_new_urls(self,page_url,soup):
        
        new_urls = set()
        links = soup.find_all('a')
        print links
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
                
        return new_urls
    
    def _get_new_data(self,soup):
        
        res_data = []
        titles = soup.find_all('a',class_='msk')
        numbers = soup.find_all('span',class_='nb')
        
        for title in titles:
            count = 0
            number = re.match(r'[1-9][0-9][0-9][0-9]{3,4}',numbers[count].get_text())
            if number:
                res_data.append(title)
                res_data.append(numbers[count].get_text())
                count+=1
            else:
                count+=1
        
        return res_data
              
    def Parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser',from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        
        return new_urls, new_data

        