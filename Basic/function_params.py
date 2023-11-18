# 여러 개의 입력값을 받는 함수 만들기

def add_many(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add_many(1, 2, 3, 4, 5)) # 15

def add_many(options, *args):
    if options == 'A':
        total = 0
        for arg in args:
            total += arg
    elif options == 'B':
        total = 1
        for arg in args:
            total *= arg
    return total

print(add_many('A', 1, 2, 3, 4, 5)) # 15
print(add_many('B', 1, 2, 3, 4, 5)) # 120



