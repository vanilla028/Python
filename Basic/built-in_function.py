# abs() - 입력받은 숫자의 절댓값을 리턴하는 함수
print(abs(-3)) # 3
print(abs(-0.034)) # 0.034

# all() - 반복문으로 순회할 수 있는(iterable) 데이터를 입력으로 받는데, 요소가 모두 참이면 True, 거짓이면 False를 반환
print(all([0, 1, 2, 3, 4, 5])) # False

# any() - 반복문으로 순회할 수 있는(iterable) 데이터를 입력으로 받는데, 요소 중 하나라도 참이면 True, 모두 거짓이면 False를 반환한다.
print(any([0, 1, 2, 3, 4, 5])) # True

# chr() - 유니코드 숫자 값을 입력으로 받아 해당하는 문자를 반환하는 함수
print(chr(86)) # V

# ord() - 문자를 입력받아 유니코드 숫자 값을 반환. <--> chr()와 반대로 동작
print(ord('b')) # 98

print(dir())
"""
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__']
"""
a = 1
b = 2
print(dir())
"""
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__', 'a', 'b']
"""
print(dir(a))

# 라이브러리, 패키지, 모듈명 입력 시 사용 가능한 함수 명단을 제공
import math
print(dir(math))
"""
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 
'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 
'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
"""

# divmod(a, b) - 두 개의 숫자 a, b를 입력으로 받아, a를 b로 나눈 몫과 나머지를 튜플로 반환한다.
print(divmod(10, 21)) # (0, 10)

# enumerate() - 순서가 있는 데이터(리스트, 튜플, 문자열)을 입력으로 받아 인덱스를 생성하여 반환한다.
for i, name in enumerate(['mimi', 'jeje', 'lala']):
    print(i, name)
"""
0 mimi
1 jeje
2 lala
"""

# eval() - 문자열로 구성된 표현식을 입력으로 받아, 실행한 결괏값을 반환한다.
print(eval("'a'+'5'")) # a5
print(eval('1+2+3+4+5')) # 15

# filter(f, iterable data) - 입력값으로 함수와 반복 가능한 데이터를 입력으로 받는다. 함수 호출시 반환값이 참인 것만 필터링하여 반환
def negative(x):
    return x < 0 
result = filter(negative, [-1, 3, 5, -7, 4, 8, 10])
print(list(result)) # [-1, -7]

# filter() -> lambda 함수 사용하여 출력하기
result = list(filter(lambda x: x < 0, [-1, 3, 5, -7, 4, 8, 10]))
print(result) # [-1, -7]

# hex() - 정수를 입력받아 16진수(hexadecimal)로 변환하여 반환
print(hex(8)) # 0x8

# id() - 객체를 입력으로 받아 고유 주소를 반환
mj = "Hello, I am MJ!"
print(id(mj)) # 2288611842864

# --- 그밖의 내장 함수들 ---

# int(), str(), len(), sum(), tuple() list(), type(), map(), max(), min(), open(), range(), sorted()
# pow(a, b) - a**b 값 반환
# round() - 숫자 입력받아 반올린하여 반환
# zip() = 동일한 개수로 이루어진 데이터를 묶어서 반환