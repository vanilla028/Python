# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

a = list(map(int, input("N개의 정수를 공백으로 구분하여 입력하세요: ").split()))
v = int(input("정수를 입력하세요: "))

result = [x for x in a if x < v]

print(f"입력된 수 중에서 {v}보다 작은 수: ")

for num in result:
    if num == result[-1]:
        print(num, end=" ")
    else:
        print(num, end=", ")

# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

number = int(input("수열을 만듭니다. 개수를 먼저 입력하세요: "))

a = [0]*number
for i in range(number):
    num = int(input("정수를 입력하세요(한 개씩 입력 후 엔터): "))
    a[i] += num

x = int(input("수열에서 x보다 작은 수를 구합니다. x를 입력하세요: "))

result = [v for v in a if v < x]
print(f"{x}보다 작은 수는 {result}입니다.")
