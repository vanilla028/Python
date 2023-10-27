# (세 자리 수) x (세 자리 수) 곱셈 과정 출력하기
a, b = map(int, input().split())
hundreds = b // 100
tens = (b % 100) // 10
ones = b % 10

print(a * ones)
print(a * tens)
print(a * hundreds)
print(f"{a}와 {b}의 곱은", a*b, "입니다." )

"""
483 752
966
2415
3381
483와 752의 곱은 363216 입니다.
"""
