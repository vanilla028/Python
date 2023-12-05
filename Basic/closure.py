# 나눗셈의 몫을 구하는 함수를 만들어 본다.
from typing import Any


def div(n):
    return n // 5

def div(n):
    return n // 7

# ===========================================
# 클래스로 만들기
class Div:
    def __init__(self, m):
        self.m = m
    
    def div(self, n):
        return n // self.m

if __name__ == "__main__":
    div5 = Div(5)
    div7 = Div(7)

    print(div5.div(25)) # 5
    print(div7.div(56)) # 8

# ==========================================
# __call__ 메서드 사용하기
class Div:
    def __init__(self, m):
        self.m = m
    
    def __call__(self,  n):
        return n // self.m

if __name__ == "__main__":
    div5 = Div(5)
    div7 = Div(7)

    print(div5(25)) # 5
    print(div7(56)) # 8

# ==========================================
# 더 간편하게 만들기 - 클로저(closure) 사용하기
def div(m):
    def inner(n):
        return n // m
    return inner

if __name__ == "__main__":
    div5 = div(5)
    div7 = div(7)

    print(div5(25)) # 5
    print(div7(56)) # 8

    
        