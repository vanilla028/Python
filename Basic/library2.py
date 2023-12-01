# 순열
from itertools import permutations
result = list(permutations(['a', 'b', 'c'], 2))
print(result)
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
import itertools
result = list(itertools.permutations(['a', 'b', 'c'], 2))
print(result)

# 조합
from itertools import combinations
result = list(combinations(['a', 'b', 'c'], 2))
print(result)
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
import itertools
result = list(combinations(['a', 'b', 'c'], 2))
print(result)

# 긴 객체에 맞춰 fillvalue 채우기
import itertools
friends = ['민아', '예솔', '성인', '민정', '수진']
foods = ['피자', '치킨', '떡']
result = itertools.zip_longest(friends, foods, fillvalue='파스타')
print(list(result))
# [('민아', '피자'), ('예솔', '치킨'), ('성인', '떡'), ('민정', '파스타'), ('수진', '파스타')]

# functools.reduce로 객체를 하나의 값으로 줄이기
import functools
data = [1, 2, 3, 4, 5, 6, 7, 8, 10]
result = functools.reduce(lambda x, y: x + y, data)
print(result) # 46

# functools.reduce로 최댓값 구하기
data = [1, 3, 5, 7, 9]
result = functools.reduce(lambda x, y: x if x > y else y, data)
print(result) # 9

# 다양한 기준으로 정렬하기
from operator import itemgetter
info = [('민정', 99.8), ('수진', 89), ('은우', 95)]
result = sorted(info, key=itemgetter(1), reverse=True)
print(result)
# [('민정', 99.8), ('은우', 95), ('수진', 89)]
# 참고: 클래스의 객체인 경우 operator.attrgetter() 사용

# 파일을 복사(copy)하거나 이동(move)하기
import shutil
shutil.copy("C:/Users/해피마미/connected_github/Python/Basic/library.py", 
            "C:/Users/해피마미/connected_github/Python/Basic/library.py.bak")

shutil.move("C:/Users/해피마미/connected_github/Python/Basic/library.py.bak",
         "c:/temp/library.py.bak")


# 디렉토리에 있는 파일들을 리스트로 만들기
import glob
path = "C:/Users/해피마미/connected_github/Python/Basic/*"
files = glob.glob(path)
print(files)
"""
['C:/Users/해피마미/connected_github/Python/Basic\\01.Print.ipynb', 
'C:/Users/해피마미/connected_github/Python/Basic\\02.Input.ipynb',
...
"""

# 객체를 파일에 저장하고 로드하기
import pickle
f = open("pk_test.txt", 'wb') # 바이너리 형식
data = {1: '강아지', 2: '고양이', 3: '햄스터', 4: '토끼', 5: '고릴라'}
pickle.dump(data, f)
f.close()

f = open("pk_test.txt", 'rb')
data = pickle.load(f)
print(data)
# {1: '강아지', 2: '고양이', 3: '햄스터', 4: '토끼', 5: '고릴라'}{1: '강아지', 2: '고양이', 3: '햄스터', 4: '토끼', 5: '고릴라'}

# 환경 변수, 디렉토리, 파일 등의 OS 자원을 제어하는 모듈
import os


# 환경 변숫값 확인하기
import os
print(os.environ)

# 디렉토리 위치 변경하기
# os.chdir()

# 디렉토리 위치 반환하기
# os.getcwd()

# 시스템 명령어 호출하기
# os.system()

# 시스템 명령어 반환하기
# os.popen()

# 여러 개의 파일을 zip 형식으로 병합 또는 해제하기
import zipfile

# 압축할 파일을 만든다
f = open("hello.txt", 'w')
data = "안녕하세요."
f.write(data)
f.close()

f = open("morning.txt", 'w')
data = "좋은 아침이에요."
f.write(data)
f.close()

with zipfile.ZipFile('zip_test.zip', 'w') as zip:
    zip.write('hello.txt')
    zip.write('morning.txt')

# with zipfile.ZipFile('zip_test.zip', 'w') as zip:
#     zip.extractall()



# 스레딩
import time

# 파일을 임시로 만들어서 사용할 때 유용한 모듈
import tempfile

# traceback
import traceback

# JSON 파일 읽고 쓰기
import json

# URL 읽고 분석할 때 사용하는 모듈
import urllib.request

# 시스템 브라우저 호출 시 사용하는 모듈
import webbrowser



