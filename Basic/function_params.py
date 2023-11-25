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

# 키워드 매개변수
def print_kwargs(**kwargs):
    print(kwargs)

# key=value 형태로 입력하면, 딕셔너리 형태로 저장된다.
print_kwargs(name='Aronamj', city='Seoul', school='Yonsei')
# {'name': 'Aronamj', 'city': 'Seoul', 'school': 'Yonsei'}

# 매개변수에 초기값 미리 설정하기
def myself(name, city, woman=True):
    print('내 이름은 %s이다.' % name)
    print('내가 사는 도시는 %s이다.' % city)
    if woman:
        print('여성입니다.')
    else:
        print('남성입니다.')

myself('Aronamj', 'Seoul')
"""
내 이름은 Aronamj이다.
내가 사는 도시는 Seoul이다.
여성입니다.
"""
