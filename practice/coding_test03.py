# 문자열로 삼각형 출력하기
def print_triangle(n):
    for i in range(1, n + 1):
        star = "*" * i
        print(star)

print_triangle(3)


import sys

def print_triangle(n):
    for i in range(n):
        star = ((i+1) * "*") 
        print(star)

n = int(sys.stdin.readline().strip())
print_triangle(n)

"""
채점 결과
정확성: 100.0
효율성: 0.0
합계: 100.0 / 100.0
"""