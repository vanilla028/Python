# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

num = list(map(int, input("N개의 정수를 공백으로 구분하여 입력하세요: ").split()))

v = int(input("찾고 싶은 정수를 입력하세요: "))
count = num.count(v)
print(f"{v}이/가 입력된 수들 중 {count}개입니다.")



