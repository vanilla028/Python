# 단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.

s = input("단어를 입력하세요: ").strip()
i = int(input("정수를 입력하세요."))
print("S의", i, "번째 글자: ", s[i-1])


# 알파벳으로만 이루어진 단어를 입력받아, 그 길이를 출력하는 프로그램을 작성하시오.
s = input("영어 단어를 입력하세요: ")
print(len(s))


# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

s = input("알파벳 소문자, 대문자, 숫자 0-9에서 원하는 것을 입력하세요: ")
ascii_value = ord(s)
print(ascii_value)


# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 문자열로 입력받는다.
num_str = input("숫자를 입력하세요: ")
total = 0

for digit in num_str:
    total += int(digit)

print(total)
