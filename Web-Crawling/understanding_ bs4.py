import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find('title')
print(result) # <title>크롤링 연습사이트 01</title>