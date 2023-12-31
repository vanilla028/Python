# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.
# 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다.
# 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.
# 도현이는 앞으로 M번 공을 넣으려고 한다. 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 
# 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다. 
# 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다.
# 공을 넣을 바구니는 연속되어 있어야 한다. 공을 어떻게 넣을지가 주어졌을 때, 
# M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.

basket, num = map(int, input("바구니 개수와 공을 넣을 횟수를 입력하세요(공백으로 분리): ").split())

# 초기 바구니 상태
baskets = [0] * basket

for i in range(num):
    start, end, ball = map(int, input(f"{i+1}번째 공을 넣을 바구니의 범위와 공 번호를 입력하세요: ").split())
    for j in range(start - 1 , end):
        baskets[j] = ball

print("각 바구니에 들어있는 공: ")
for i, ball in enumerate(baskets):
    print(f"바구니 {i+1}: {ball}")


"""
바구니 개수와 공을 넣을 횟수를 입력하세요(공백으로 분리): 5 3
1번째 공을 넣을 바구니의 범위와 공 번호를 입력하세요: 1 5 3
2번째 공을 넣을 바구니의 범위와 공 번호를 입력하세요: 2 3 5
3번째 공을 넣을 바구니의 범위와 공 번호를 입력하세요: 4 5 1
각 바구니에 들어있는 공: 
바구니 1: 3
바구니 2: 5
바구니 3: 5
바구니 4: 1
바구니 5: 1
"""
