import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')
picks = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a')

for p in picks:
    print(p.text)
    
print(p)