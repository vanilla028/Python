# 클래스 연습

class Calculator:

    def __init__(self):
        self.result = 0
    
    def set_nums(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def square(self):
        result = self.first ** self.second
        return result

a = Calculator()
b = Calculator()

a.set_nums(3, 5)
a.add() # 8

b.set_nums(2, 8)
b.sub() # -6

# 입력받을 매개변수의 개수를 알 수 없을 때: *args 가변인수 사용
class Calculator:
    def set_nums(self, *args):
        self.numbers = list(args)
    
    def add(self):
        result = sum(self.numbers)
        return result
    
    def sub(self):
        result = self.numbers[0] - self.numbers[1:]
        return result
    
    def div(self):
        result = self.first / self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def square(self):
        result = self.first ** self.second
        return result   

a = Calculator()
a.set_nums(1, 2, 3, 4, 5, 6, 7, 8)
a.add() # 36