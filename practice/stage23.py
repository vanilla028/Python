# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 
# 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다.
# 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 
# 따라서, 상수는 두 수 중 큰 수인 437을 큰 수라고 말할 것이다.
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

# a, b = map(int, input("세 자리 숫자 두 개를 입력하세요: ").split())
a = "354"
b = "251"

# a
a_list = [i for i in a]
print(a_list) # ['3', '5', '4']

reversed_a_list = a_list[::-1] # 시작~끝까지 역순으로 슬라이싱
print(reversed_a_list) # ['4', '5', '3']

# 다시 숫자로 만들기
result_a = ''.join(reversed_a_list)
print(result_a) # 453


# b
b_list = [i for i in b]
print(b_list) # ['2', '5', '1']

reversed_b_list = b_list[::-1] # 시작~끝까지 역순으로 슬라이싱
print(reversed_b_list) # ['1', '5', '2']

# 다시 숫자로 만들기
result_b = ''.join(reversed_b_list)
print(result_b) #152

if result_a > result_b:
    print(f"큰 수는 {result_a}입니다!")
else:
    print(f"큰 수는 {result_b}입니다!")

