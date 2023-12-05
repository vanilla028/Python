class Iterator:
    def __init__(self, num_list):
        self.num_list = num_list
        self.position = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.num_list):
            raise StopIteration # 예외 발생시키기
        result = self.num_list[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    factors = Iterator([2, 4, 6, 8, 10])
    for factor in factors:
        print(factor)

"""
2
4
6
8
10
"""

# 역순 이터레이터 클래스
class Iterator:
    def __init__(self, num_list):
        self.num_list = num_list
        self.position = len(self.num_list) -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0:
            raise StopIteration # 예외 발생시키기
        result = self.num_list[self.position]
        self.position -= 1
        return result

if __name__ == "__main__":
    factors = Iterator([2, 4, 6, 8, 10])
    for factor in factors:
        print(factor)

"""
10
8
6
4
2
"""