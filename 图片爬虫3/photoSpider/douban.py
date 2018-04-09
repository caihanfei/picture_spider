import requests
import re
content = requests.get('https://book.douban.com/').text
pattern = re.compile('<a href="?(.+?)" title="?(.+?)>?')
result = re.findall(pattern,content)

for i in result:
    print i