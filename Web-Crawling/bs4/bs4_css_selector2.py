import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/02/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

result4 = soup.select("a[href]")
result5 = soup.select('a[href$=".net"]') # $ 해당 값으로 끝나는 것
result6 = soup.select('a[href^=".net"]') # $ 해당 값으로 시작하는 것
result7 = soup.select('a[href*=".net"]') # $ 해당 값을 포함하는 것
result8 = soup.select('a[href~=".net"]') # $ 해당 값과 일치하는 것

# 속성으로 찾기
result9 = soup.select('div#winter  p')
# find 함수로 찾기
result10 = soup.find(id='winter').find_all('p')

# 자식 태그만 가져오고 싶을 때
result11 = soup.select('div#winter > p')


print(result4[0].text) # 네이버
print(result5) # [<a href="http://daum.net" target="_self">다음</a>]