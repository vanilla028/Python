# 1 Hello World!를 출력하시오.
print("Hello, world!")

# 2 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split()) # 공백 문자를 기준으로 문자열 분할
print(a+b)

# 3 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
if a > 0:
    if b <10:
        print(a-b)
    else:
        print("error!")

# 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
