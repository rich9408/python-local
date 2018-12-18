import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=sugsch&w=tot&DA=GIQ&sq=%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC&o=4&sugo=15&q=%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC+%EC%88%9C%EC%9C%84"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
notices = soup.select('#abtColl > div.coll_cont > div > div.tab_body > div:nth-of-type(1) > div > table tbody tr')

for notice in notices:
    print(notice.select_one("td:nth-of-type(1) strong").text)
    print(notice.select_one("td:nth-of-type(1) span").text)
    print(notice.select_one("td:nth-of-type(2)").text)
    #print(notice.select_one("td:nth-of-type(1) strong").text)
    #print(notice.select_one("td:nth-of-type(1) strong").text)