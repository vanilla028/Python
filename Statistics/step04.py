import numpy as np
import matplotlib.pyplot as plt

# 베르누이 분포 시뮬레이션
p = 0.8  # 성공 확률
n = 1000  # 시행 횟수
random_samples = np.random.binomial(1, p, n)

# 결과 시각화
plt.hist(random_samples, bins=[0, 1, 2], align='left')
plt.xticks([0, 1], ['fail', 'success'])
plt.xlabel('result')
plt.ylabel('frequency')
plt.title("Bernoulli's trials")
plt.show()
