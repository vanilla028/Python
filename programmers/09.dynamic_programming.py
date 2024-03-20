def solution(tri):
    # 삼각형의 높이
    height = len(tri)

    # 배열 초기화
    # [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
    dp = [[0] * (i + 1) for i in range(height)]
    dp[0][0] = tri[0][0]

    # 최대값을 계산하여 dp 배열에 저장
    for i in range(1, height):
        for j in range(i + 1):
            # [1][0] >> [2][0] or [2][1]
            # [1][1] >> [2][1] or [2][2]
            if j == 0:
                dp[i][j] = dp[i - 1][j] + tri[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]

    # 최대값 반환
    return max(dp[height - 1])

# 예시 삼각형 배열
example = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

# 거쳐간 숫자의 최댓값 출력
print(solution(example))  # Output: 30
