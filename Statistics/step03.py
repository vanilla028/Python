import numpy as np
from scipy.stats import chi2_contingency

# 분할 표 생성
data = np.array([[10, 20, 30], [50, 60, 70]])

# 카이제곱 검정(Chi-Squre Test): 범주형 데이터의 연관성을 검정
# Degree of Freedom
chi2, p_value, dof, expecte = chi2_contingency(data)

# 결과 출력
print("카이제곱 통계량: ", chi2)
print("p-value: ", p_value)

if p_value < 0.05:
    print(f"p값 {p_value:.2f}, 귀무 가설을 기각합니다.")
else:
    print(f"p값 {p_value:.2f}, 귀무 가설을 기각하지 않습니다.")

"""
카이제곱 통계량:  3.555555555555556
p-value:  0.16901331540606604
p값 0.17, 귀무 가설을 기각하지 않습니다.
"""
import pandas as pd

data2 = {
    '성별': ['남성', '여성', '남성', '여성', '남성', '여성', '남성', '여성'],
    '커피종류': ['커피 A', '커피 B', '커피 A', '커피 B', '커피 C', '커피 B', '커피 A', '커피 C']
}

df = pd.DataFrame(data2)

# contingency table 생성
contingency_table = pd.crosstab(df['성별'], df['커피종류'])

# 카이제곱 검정 수행
chi2, p, dof, expected = chi2_contingency(contingency_table)

# 결과 출력
print("카이제곱 통계량: ", chi2)
print("p-value: ", p)
print("자유도: ", dof)
print("기대값: ", expected)

# p-value와 유의수준 비교
if p < 0.05:
    print(f"p-값 {p:.2f}, 귀무 가설을 기각합니다. 성별과 커피 선호도 간에 통계적으로 유의미한 연관성이 있습니다.")
else:
    print(f"p-값 {p:.2f}, 귀무가설을 기각하지 않습니다. 성별과 커피 선호도 간에 통계적으로 유의미한 연관성이 없습니다.")

"""
카이제곱 통계량:  6.0
p-value:  0.04978706836786395
자유도:  2
기대값:  [[1.5 1.5 1. ]
 [1.5 1.5 1. ]]
p-값 0.05, 귀무 가설을 기각합니다. 성별과 커피 선호도 간에 통계적으로 유의미한 연관성이 있습니다.
"""
