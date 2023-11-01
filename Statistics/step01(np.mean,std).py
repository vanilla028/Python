import numpy as np

# 1차원 배열 데이터 생성
data = np.array([10, 23, 27, 42, 37, 25, 28, 35])

# 데이터의 평균 계산
mean = np.mean(data)
print("평균: ", mean)

# 데이터의 중앙값 계산
# 데이터에 이상치가 있는 경우, 중앙값이 평균보다 더 신뢰할 수 있는 대표값일 수 있다.
median = np.median(data)
print("중앙값: ", median)

# 데이터의 표준 편차 계산
std_dev = np.std(data)
print("표준 편차: ", std_dev)

"""
평균:  28.375
중앙값:  27.5
표준 편차:  9.245776062613674
"""

