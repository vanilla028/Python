# 스레딩
import time

def task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)

print("Start...")

# for i in range(5):
#     task()

print("End")
# ===> 총 25초의 시간이 걸린다

import threading

def task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)

print("Start...")

threads = []
for i in range(5):
    t = threading.Thread(target=task)
    threads.append(t)

# for t in threads:
#     t.start()

print("End")
# ===> Start, End가 먼저 출력되고 스레드 결과가 출력된다.

def task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)

print("Start...")

threads = []
for i in range(5):
    t = threading.Thread(target=task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("End")
# ===> 정상적으로 "Start..."가 출력된 뒤 스레드가 출력되고 마지막으로 "End"가 출력된다.

# 파일을 임시로 만들어서 사용할 때 유용한 모듈
import tempfile

# traceback
import traceback
# traceback 모듈의 format_exc()는 오류 추적 결과를 문자열로 반환한다.
# 오류가 발생한 위치에 다음 문장 추가 print(traceback.format_exc())

# JSON 파일 읽고 쓰기
import json
# 딕셔너리 변환
with open('bla.json') as f:
    data = json.load(f)
type(data)
# 파일 생성
data = {'a': '수학', 'b': '영어'}
with open('bla.json', 'w') as f:
    json.dump(data, f)

# JSON으로 변환
json_data = json.dumps(data)

# 아스키 형태의 문자열로 변경되는 것 방지하기
json_data = json.dumps(data, ensure_ascii=False) # indent 옵션으로 들여쓰기도 가능

# URL 읽고 분석할 때 사용하는 모듈
import urllib.request

# 시스템 브라우저 호출 시 사용하는 모듈
import webbrowser
webbrowser.open_new('http://applepy.tistory.com')
webbrowser.open('http://www.naver.com')
