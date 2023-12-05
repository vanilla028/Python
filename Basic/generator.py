# 제너레이터(generator)?
# ==> 이터레이터(iterator)를 생성해 주는 함수

def generator():
    yield 1
    yield 2
    yield 3

a = generator()
print(type(a)) # <class 'generator'>
print(next(a)) # 1
print(next(a)) # 2
print(next(a)) # 3
# print(next(a)) # 값이 없으므로 StopIteration 예외가 발생한다.

def generator():
    for i in range(1, 10):
        result = i * i # 각각의 숫자를 제곱
        yield result

b = generator()

print(next(b)) # 1
print(next(b)) # 4
print(next(b)) # 9
print(next(b)) # 16
print(next(b)) # 25
print(next(b)) # 36

# b = (i * i for i in range(1, 10)) 튜플 표현식으로도 쓸 수 있다.
# 리스트 컴프리헨션 구문과 유사. 제너레이터 표현식


import time

def job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (job() for i in range(5))
print(next(list_job)) # job start

# 제너레이터의 유용성? ==> 시간이 오래 걸리는 작업을
# 한꺼번에 처리하기보다는 필요한 경우에 호출하여 사용


