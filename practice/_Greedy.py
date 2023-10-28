# 그리디
# 어떠한 수 N이 1이 될 때까지 두 가지를 반복적으로 수행한다.
# 1. N에서 1을 뺀다.
# 2. N을 k로 나눈다. N이 K로 나누어떨어질 때만 수행할 수 있다.
# 최소 횟수를 구한다.

n, k = map(int, input("숫자 N과 K를 입력하세요: ").split())

result = 0
while n >= k:
    if n % k != 0:
        n -= 1
        result += 1
        n //= k
        result += 1
    else:
        n //= k
        result += 1

while n > 1:
    n -= 1
    result += 1

print(result) 
    
