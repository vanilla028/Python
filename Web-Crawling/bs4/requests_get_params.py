# get 방식으로 데이터 전달하기
import requests

url = 'https://www.naver.com'

params = {'data1':'data1', 'data2':'data2'}

response = requests.get(url, params=params) # == https://www.naver.com/?data1=data1&data2=data2'

# print(response.status_code) # 200
# print(response.text) # <!doctype html>로 시작하는 HTML 문서가 출력된다.

print(response.url) # https://www.naver.com/?data1=data1&data2=data2