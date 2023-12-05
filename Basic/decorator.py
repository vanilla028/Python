# 함수 실행 시간 측정하기
import time

def check():
    start = time.time()
    print("함수 실행 Start..")
    for i in range(5):
        print("함수가 실행 중입니다.")
    end = time.time()
    print("함수 수행시간: %f 초" % (end-start))

check()
"""
함수 실행 Start..
함수가 실행 중입니다.
함수가 실행 중입니다.
함수가 실행 중입니다.
함수가 실행 중입니다.
함수가 실행 중입니다.
함수 수행시간: 0.000996 초
"""
# ===> 실행 시간을 측정해햐 하는 함수가 많다면, 비효율적.
# 클로저를 사용하여 효율적으로 만든다. check_time 함수 == 데코레이터

def check_time(func):
    def inner():
        start = time.time()
        result = func()
        end = time.time()
        print("함수 수행시간: %f 초" % (end-start))
        return result
    return inner

def a():
    for i in range(5):
        print("안녕하세요!")

def b():
    for i in range(3):
        print("날씨가 좋네요!")

func1 = check_time(a)
func2 = check_time(b)
func1()
func2()
    
"""
안녕하세요!
안녕하세요!
안녕하세요!
안녕하세요!
안녕하세요!
함수 수행시간: 0.000996 초

날씨가 좋네요!
날씨가 좋네요!
날씨가 좋네요!
함수 수행시간: 0.000000 초
"""


# 데코레이터(decorator)
def check_time(func):
    def inner():
        start = time.time()
        result = func()
        end = time.time()
        print("함수 수행시간: %f 초" % (end-start))
        return result
    return inner

@check_time
def a():
    for i in range(5):
        print("안녕하세요!")

@check_time
def b():
    for i in range(3):
        print("날씨가 좋네요!")

a()
b()

# 간소화되었다.