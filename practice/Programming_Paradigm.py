# 절차지향 프로그래밍(Procedural Programming)

# 데이터: 두 개의 정수
num1 = 5
num2 = 3

# 함수 정의
def add_and_print():
    result = num1 + num2
    print(f"결과는 {result}입니다.")

# 함수 호출
add_and_print()


# 객체 지향 프로그래맹(Object-Oriented Programming)

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add_and_print(self):
        result = self.num1 + self.num2
        print(f"결과: {result}")

# 객체 생성

calc = Calculator(5, 3)
calc.add_and_print()
