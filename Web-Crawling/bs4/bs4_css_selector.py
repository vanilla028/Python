import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/02/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

result = soup.select("#title")
result1 = soup.select_one("title")
result2 = soup.select(".blue") # class
result3 = soup.select("#title.bold.blue")


print(result) # 리스트로 출력
"""
[<div class="bold blue" id="title">
        안녕하세요
    </div>]
"""

print(result1) # <title>크롤링 연습사이트 02</title>

print(result2)

print(result3)
"""
[<div class="bold blue" id="title">
        안녕하세요
    </div>]
"""