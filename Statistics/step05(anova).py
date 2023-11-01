from scipy.stats import f_oneway

# 예시 데이터 (세 개의 그룹)
group1 = [45, 50, 55, 60, 65]
group2 = [55, 60, 65, 70, 75]
group3 = [65, 70, 75, 80, 85]

# ANOVA 수행
f_statistic, p_value = f_oneway(group1, group2, group3)

# 결과 출력
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# P-value와 유의수준(예: 0.05) 비교
alpha = 0.05
if p_value < alpha:
    print("그룹 간에 통계적으로 유의미한 차이가 있습니다.")
else:
    print("그룹 간에 통계적으로 유의미한 차이가 없습니다.")

"""
F-statistic: 8.0
P-value: 0.0061963977594369675
그룹 간에 통계적으로 유의미한 차이가 있습니다.
"""
# ==> 유의미한 차이가 있으므로 사후 분석이 필요하다.
# 다양한 방법이 있는데, Dunntt's 법의 경우 하나의 그룹을 기준으로 다른 그룹 비교하는 방식이다.