# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

a = int(input("구구단 자동 계산기입니다. 원하는 단을 입력하세요: "))

for i in range(1, 10):
    print(f"{a} x {i} = {a * i}")

"""
구구단 자동 계산기입니다. 원하는 단을 입력하세요: 8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
"""


# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

t = int(input("출력할 개수를 입력하세요: "))

for i in range(1, t+1):
    a, b = map(int, input("숫자 두 개를 입력하면, 두 수를 더한 결과를 출력합니다: ").split())
    print(a+b)


# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
n = int(input("1부터 n까지의 합을 구합니다. n을 입력하세요: "))
total = 0
for i in range(1, n+1):
    total += i

print(total)


# 영수증에 적힌 내용을 보고 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
# - 구매한 각 물건의 가격과 개수
# - 구매한 물건들의 총 금액

receipt = int(input("영수증 금액 합계를 입력하세요: "))
num = int(input("품목의 개수를 입력하세요: "))

total = 0
for i in range(num):
   price, num = map(int, input("각 물건의 가격과 개수를 입력하세요(공백으로 분리): ").split())
   price = price * num
   total += price

if receipt == total:
    print("금액이 일치합니다.")
else:
    print(f"금액이 일치하지 않습니다. 영수증 총 금액은 {receipt}원이고, 품목별로 계산한 금액은 {total}원입니다.")


# 빠른 A+B
import sys
a, b = map(int, sys.stdin.readline().strip().split())
print(a+b)

