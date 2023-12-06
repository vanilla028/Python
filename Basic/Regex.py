# 정규 표현식(Regular Expressions)


# 메타 문자:
# []
# [abc] ==> a, b, c 중 어느 한 개의 문자와 매치되는 경우
# [a-c] ==> 범위 지정. 위와 동일
# [a-zA-Z] ==> 모든 알파벳
# [0-9] ==> 모든 숫자

# [^]
# [^0-9] ==> ^는 not의 의미. 숫자가 아닌 문자 매치

# \d == [0-9]
# \w == [a-zA-Z0-9_]
# \D == [^0-9]
# \W == [^a-zA-Z0-9_] 

# \s == 화이트스페이스 문자와 매치. [\t\n\r\f\v]
# \t 탭
# \n 줄바꿈
# \r 강제 줄바꿈
# \f 페이지 나눔
# \v 수직 탭

# . ==> \n 제외한 모든 문자와 매치
# a.b ==> a와 b 사이에 어떤 문자가 들어가든 매치가 된다. abc (X)
# a[.]b ==> [] 안에 .를 쓰면 메타문자가 아니라 문자 그대로를 의미한다.

# *
# a*b ==> a가 0부터 무한대까지 반복되는 경우 매치

# a+b ==> a가 1번 이상 반복되어 매치 ab aab aaab

# 반복횟수 제한하기
# a{3}b ==> a가 반드시 3번 반복되는 경우 매치 aaab
# a{2,}b ==> a의 반복 횟수가 2 이상인 경우 매치 aab aaab
# a{, 2}b ==> a의 반복 횟수가 2 이하인 경우 매치 ab aab
# a{3,5}b ==> a의 반복 횟수가 3이상 5이하인 경우 매치

# a?b == a{0, 1}b a가 0개 또는 1개인 경우 매치

# 파이썬에서 정규 표현식 사용법

import re

c = re.compile('[a-zA-Z]+')

# re 라이브러리의 메서드

# match
# 문자열의 처음부터 검색.
m = c.match("Ariana Grande")
print(m) # Ariana

m2 = c.match("888Ariana Grande")
print(m2) # None

# search
# 문자열의 처음부터 검색 X. 문자열 전체를 검색한다.
s = c.search("888Ariana Grande")
print(s) # Ariana

# findall
f = c.findall("Ariana Grande")
print(f) # ['Ariana', 'Grande'] ==> 매치되는 모든 값 반환

# finditer
# 반복 가능한 객체 반환
t = c.finditer("Ariana Grande is cute.")
for i in t: print(i)
"""
<re.Match object; span=(0, 6), match='Ariana'>
<re.Match object; span=(7, 13), match='Grande'>
<re.Match object; span=(14, 16), match='is'>
<re.Match object; span=(17, 21), match='cute'>
"""

# Group - match
g = c.match("I like coding!")
print(g.group()) # I
print(g.start()) # 0 문자열의 시작 위치
print(g.end()) # 1 문자열의 끝 위치
print(g.span()) # (시작, 끝) 튜플 반환

# Group - search
h = c.search("888 I like codint!")
print(h.group()) # I
print(h.start()) # 4 문자열의 시작 위치
print(h.end()) # 5 문자열의 끝 위치
print(h.span()) # (시작, 끝) 튜플 반환

# 코드 축약하기
c = re.compile('[a-zA-Z]+')
m = c.match("I like Python!")

# ===> 다음과 같이 한 줄로 축약 가능!
p = re.match('[a-zA-Z]+', "I like Python!")

# 컴파일 옵션(-ing)

# DOTALL
# IGNORECASE
# MULTILINE
# VERBOSE
# 역슬래시 문제


