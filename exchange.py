import requests
from bs4 import BeautifulSoup

url = "http://www.kita.net/exchangeRate_info/exchangeRate_info_list.jsp"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
notices = soup.select('#kitacont > div.trends > div > table > tbody tr')
#print(notices)
for notice in notices:
    print('------------------')
    print(notice.select_one("th").text)
    print(notice.select_one("td:nth-of-type(1)").text)