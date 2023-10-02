from bisect import bisect_left, bisect_right

def count(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 정렬된 리스트
a = [5, 7, 7, 7, 8, 8, 9, 10, 15]

# 값이 7인 데이터 개수 출력
print(count(a, 7, 7))

# 값이 [-1, 7] 범위에 있는 데이터 개수 출력
print(count(a, -1, 7))