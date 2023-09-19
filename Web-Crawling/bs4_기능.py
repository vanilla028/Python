import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find('title')
result1 = soup.find_all('p',limit=2)
result2 = soup.find("th", "tablehead")
result3 = soup.find('a')

print(result) # <title>크롤링 연습사이트 01</title>
print(result.text) # text만 가져오기 # 크롤링 연습사이트 01

print(result1)
print(result2)
print(result3) # <a href="01.html">1페이지 바로가기</a>
print(result3.attrs['href']) # 01.html