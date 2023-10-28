# 이진 탐색
# 부품이 N개 있을 때, 각 부품은 정수 형태의 고유한 번호가 있다.
# 손님이 문의한 부품 M게 종류를 모두 확인해서 견적서를 작성해야 한다.
# N = 5
# 부품 번호는 [4, 2, 7, 8, 1]
# 이때손님이 요청한 부품 번호의 순서대로 부품을 확인해,
# 부품이 있으면 yes, 없으면 no를 출력한다. 구분은 공백으로 한다.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# 부품 번호 리스트를 정렬합니다.
parts = [4, 2, 7, 8, 1, 2]
parts.sort()

# 손님이 요청한 부품 번호 리스트
requested_parts = [4, 1, 3]

result = []
for part in requested_parts:
    if binary_search(parts, part):
        result.append("yes")
    else:
        result.append("no")

# 결과 출력
print(" ".join(result))
#=====================================================================
# 집합으로 풀기

# 입력받을 때
# n = int(input())
# array = set(map(int, input().split()))
# requested_parts = list(map(int, input().split())))

n = 5
array = [4, 2, 7, 8, 1, 2]
requested_parts = [7, 8]

array = set(array)
print(array) # {1, 2, 4, 7, 8}

for i in requested_parts:
    # 부품이 있는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# yes yes