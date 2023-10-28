# 구현
# 여행가 A는 N X N 크기의 정사각형 공간 위에 있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다.
# A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
# L: 왼쪽 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위로 한 칸 이동
# D: 아래로 한 칸 이동
# 공간을 벗어나는 움직임은 무시된다.

# 입력 예시
# 공간의 크기: 5
# 계획: R R R U D D

# 최종적으로 지점의 좌표를 출력한다.

num = int(input())
plans = input().split()

# 시작 위치
x, y = 1, 1

# 이동 방향 정의
# L: (0, -1), R: (0, 1), U: (-1, 0), D: (1, 0)
dx = [0, 0, -1, 1] # L R U D
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(types)):
        if plan == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
     # 만약 공간을 벗어나면 이동을 무시한다.
    if nx < 1 or ny <1 or nx > num or ny > num:    
        continue        # 다음 계획으로 넘어간다.
    x, y = nx, ny

print(x, y)        

    





