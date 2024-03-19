# numbers 는 정수 배열 [X, XX, X, ...]
def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer <= n:
            answer += i
    return answer

print(solution([3, 5, 6, 7, 10], 22))
