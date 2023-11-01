import numpy as np
from scipy import stats # scipy의 stats: 통계 함수, 확률 분포, 통계 검정 제공 모듈

# 1차원 배열 데이터 생성
data = np.array([10, 23, 27, 42, 37, 25, 28, 35])

# 데이터의 평균 계산
mean = np.mean(data)
print("평균: ", mean)

# 데이터의 중앙값 계산
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