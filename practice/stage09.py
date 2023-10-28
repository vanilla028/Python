# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

a, b, c, = map(int, input("주사위 세 개를 굴려서 나온 숫자를 입력하시오: ").split())

# if a == b == c:
#     reward = 10000 + a * 1000
# elif a == b:
#     reward = 1000 + a * 100
# elif a == c:
#     reward = 1000 + a * 100
# elif b == c:
#     reward = 1000 + b * 100
# else:
#     reward = max(a, b, c) * 100

# print(f"보상은 {reward}원입니다.")

# 코드 간소화
if a == b == c:
    reward = 10000 + a * 1000
elif a == b or a == c or b == c:
    value = a if a == b or a == c else b
    reward =  1000 + value * 100
else:
    reward = max(a, b, c) * 100

print(f"보상은 {reward}원입니다.")
