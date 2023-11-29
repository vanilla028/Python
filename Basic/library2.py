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

# 객체를 하나의 값으로 줄이기
import functools

# 최댓값 구하기

# 다양한 기준으로 정렬하기


import shutil
# 파일을 복사(copy)하거나 이동(move)하기

import glob
# 디렉터리에 있는 파일들을 리스트로 만들기

import pickle
# 객체를 파일에 저장하고 로드하기

import os
# 환경 변수, 디렉토리, 파일 등의 OS 자원을 제어하는 모듈

# 환경 변숫값 확인하기

# 디렉토리 위치 변경하기

# 디렉터리 위치 반환하기

# 시스템 명령어 호출하기

# 시스템 명령어 반환하기

# 여러 개의 파일을 zip 형식으로 병합 또는 해제하기

import time
# 스레딩

import tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈

# traceback

import json
# JSON 파일 읽고 쓰기

import urllib.request
# URL 읽고 분석할 때 사용하는 모듈

import webbrowser



