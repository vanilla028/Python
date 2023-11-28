import datetime

# 두 날짜의 차이 구하기
day1 = datetime.date(2022, 9, 30)
day2 = datetime.date(2023, 3, 22)

period = day2 - day1
print(period) # 173 days, 0:00:00
print(period.days) # 173

# 요일 구하기 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일
day = datetime.date(2024, 10, 28)
print(day) # 2024-10-28
print(day.weekday()) # 0

import time

# 반환된 현재 시간(초 단위)을 '연, 월, 일, 시, 분, 초' 형태로 바꾸기
now = time.localtime(time.time())
print(now) # time.struct_time(tm_year=2023, tm_mon=11, tm_mday=28, tm_hour=23, tm_min=58, tm_sec=28, tm_wday=1, tm_yday=332, tm_isdst=0)
# 그 밖에 관련된 시간 함수가 있으니 필요에 따라 서치할 것.

import math

# 최대공약수 구하기
# Q.포도맛 사탕 60개, 딸기맛 사탕 100개, 오렌지맛 사탕 80개가 있다.
# 최대 몇 봉지를 만들 수 있는가? *남기지 않고 모두 담는다.
# print(math.gcd(60, 100, 80)) # 20

import random

