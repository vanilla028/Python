n = int(input())
array =[]
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True) # 내림차순
for i in array:
    print(i, end=' ') # 숫자 사이 공백으로 출력

# n에 3 입력
# 2
# 4
# 5
# 출력 결과: 5 4 2