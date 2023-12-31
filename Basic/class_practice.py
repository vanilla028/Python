# 클래스 연습

class MyCalculator:

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

a = MyCalculator()
b = MyCalculator()

a.set_nums(3, 5)
print(a.add()) # 8

b.set_nums(2, 8)
print(b.sub()) # -6

# 입력받을 매개변수의 개수를 알 수 없을 때: *args 가변인수 사용
class ManyCalculator:
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

a = ManyCalculator()
a.set_nums(1, 2, 3, 4, 5, 6, 7, 8)
print(a.add()) # 36

# 클래스의 상속
class NewCalculator(MyCalculator):
    pass

c = NewCalculator()
c.set_nums(4, 5)
print(c.add()) # 9

import math
class NewCalculator(MyCalculator):
    def mix(self):
        result = self.first + self.second
        root_result = math.sqrt(result)
        final_result = round(root_result, 4)
        return final_result

d = NewCalculator()
d.set_nums(5, 8)
print(d.mix()) # 3.6056



        
