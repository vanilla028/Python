# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다.
# 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다. 
# 도현이는 앞으로 M번 바구니의 순서를 역순으로 만들려고 한다. 
# 도현이는 한 번 순서를 역순으로 바꿀 때, 순서를 역순으로 만들 범위를 정하고, 
# 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.
# 바구니의 순서를 어떻게 바꿀지 주어졌을 때, M번 바구니의 순서를 역순으로 만든 다음, 
# 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.

n = int(input("바구니는 총 몇 개입니까? "))
baskets = list(range(1, n+1))
# print(baskets)

m = int(input("바구니의 순서를 바꿀 횟수를 입력하세요: "))



for _ in range(m):
    a, b = map(int, input("순서를 역순으로 바꿀 바구니의 범위를 입력하세요: ").split())
    baskets[a-1:b] = reversed(baskets[a-1:b])

for basket in baskets:
    if basket == baskets[-1]:
        print(basket, end=" ")
    else:
        print(basket, end=", ")

