import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")


for tag in soup.find_all('a'):
    result = requests.get('https://crawlingstudy-dd3c9.web.app/01/' + tag.attrs['href'])
    soup = BeautifulSoup(result.text, "html.parser")
    print(soup.find('p').text.strip())

# 모든 a 태그 찾기 -> 각각의 링크에 들어가서 p태그 프린트하기
# strip 양쪽 공백 정리
"""
크롤링 연습사이트 01-1 페이지입니다.
크롤링 연습사이트 01-2 페이지입니다.
크롤링 연습사이트 01-3 페이지입니다.
크롤링 연습사이트 01-4 페이지입니다.
"""

