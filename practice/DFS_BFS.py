# DFS(Depth-First Search) - 깊이 우선 탐색
# 스택(Stack) 또는 재귀 함수(Recursive Function)로 구현

# BFS(Breadth-First Search) - 너비 우선 탐색
# 큐(Queue)를 사용하여 구현. 최단 경로를 찾을 때 효과적

#=====================================================================
# 덱(deque) 자료구조를 사용한다.
from collections import deque

queue = deque()

queue.append(5)
queue.append(7)
queue.append(1)
queue.popleft()
queue.append(8)

print(queue)
queue.reverse()
print(queue)

"""
deque([7, 1, 8])
deque([8, 1, 7])
"""
# 리스트 자료형으로 반환하기
print(list(queue)) # [8, 1, 7]

# 재귀 함수?
def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function()

# recursive_function()

# 재귀 함수에 종료 조건 추가하기
def recursive_function(i):
    if i == 10:
         return # i가 10일 때 함수를 종료
    print("재귀 함수를 호출합니다.")
    recursive_function(i + 1) # 재귀 호출

recursive_function(1) # 9번만 출력되고 함수가 종료된다.

# n! 팩토리얼 구하기
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))
# n = 5이면
# 5*factorial_recursive(4)
# 4*factorial_recursive(3)
# 3*factorial_recursive(2)
# 2*factorial_recursive(1)
# 1 ==> 1
# 결과적으로 120이 반환된다.
# =====================================================================

# DFS(Depth-First Search) - 깊이 우선 탐색
# 인점한 노드 중 가장 작은 노드부터~가장 깊이 위치한 노드에 인접할 때까지 탐색한다.
# 인접 행렬

adj_mtx = 999999999 # 정답이 될 수 없는 큰 값 설정

# 2차원 리스트로 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, adj_mtx],
    [5, adj_mtx, 0]
]

print(graph) # [[0, 7, 5], [7, 0, 999999999], [5, 999999999, 0]]

# 예제
def dfs(graph, v, visited):
    visited[v] = True # 현재 노드 방문 처리
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],         # 0번 노드는 사용하지 않음 (인덱스 0 무시)
    [2, 3],     # 1번 노드와 연결된 노드
    [1, 4, 7],  # 2번 노드와 연결된 노드
    [1],        # 3번 노드와 연결된 노드
    [2, 5, 7],  # 4번 노드와 연결된 노드
    [],         # 5번 노드와 연결된 노드 없음
    [4],        # 6번 노드와 연결된 노드
    [2, 4]      # 7번 노드와 연결된 노드
]
visited = [False] * len(graph)

# 이제 함수를 호출해보자
dfs(graph, 1, visited) # 1 2 4 5 7 3

# BFS(Breadth-First Search) - 너비 우선 탐색
# 가까운 것들을 모두 큐에 삽입하고 방문처리한다.

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 현재 노드를 방문 처리
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],         # 0번 노드는 사용하지 않음 (인덱스 0 무시)
    [2, 3],     # 1번 노드와 연결된 노드
    [1, 4, 7],  # 2번 노드와 연결된 노드
    [1],        # 3번 노드와 연결된 노드
    [2, 5, 7],  # 4번 노드와 연결된 노드
    [],         # 5번 노드와 연결된 노드 없음
    [4],        # 6번 노드와 연결된 노드
    [2, 4]      # 7번 노드와 연결된 노드
]

visited = [False] * len(graph)

# 이제 함수를 호출해보자
bfs(graph, 1, visited) # 1 2 3 4 7 5