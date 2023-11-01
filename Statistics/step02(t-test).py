import numpy as np
from scipy import stats # scipy의 stats: 통계 함수, 확률 분포, 통계 검정 제공 모듈

# 두 개의 가상 데이터 집합 생성
data1 = np.array([12, 14, 17, 29, 47])
data2 = np.array([15, 28, 30, 45, 68])

# t-검정(t-test) 수행하기
t_stat, p_value = stats.ttest_ind(data1, data2)

# 결과 출력
print("t-통계량(t-statisctc): ", t_stat)
print("p-값(p-value): ", p_value)

if p_value < 0.05:
    print(f"p-값 {p_value:.2f}, 두 데이터 집합은 통계적으로 유의미한 차이가 있다.")
else:
    print(f"p-값 {p_value:.2f}, 두 데이터 집합은 통계적으로 유의미한 차이가 없다.")

# t-통계량(t-statisctc):  -1.2019991929551457
# p-값(p-value):  0.26373378780275464
# p-값 0.26, 두 데이터 집합은 통계적으로 유의미한 차이가 없다.

# ==> 유의확률이 유의수준보다 크다.
# *유의확률: 실제로는 H0가 참인데도 불구하고, H1이라고 잘못 선택할 확률(제1종 오류를 범할 확률)을 의미.