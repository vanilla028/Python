import requests

url = 'https://www.naver.com'

response = requests.get(url)

print(response.status_code) # 200
print(response.text) # <!doctype html>로 시작하는 HTML 문서가 출력된다.

# get 방식으로 데이터 전달하기
