import time

class Dog:
    def __init__(self, name, color):
        self.hungry = 0
        self.name = name
        self.color = color
    
    def eat(self):
        self.hungry += 1
        
        if self.hungry < 1:
            print("너무 배고파요ㅠㅠ")
            print("배고픔 정도: ", self.hungry)
        elif 0 < self.hungry <= 5:
            print("에너지 충전!")
            print("배고픔 정도: ", self.hungry)
        else:
            print("배불러요!")
            print("배고픔 정도: ", self.hungry)
            print("산책을 시켜주세요.")
    
    def walk(self):
        self.hungry -= 1

        if self.hungry >= 0:
            print("산책 좋아. 멍멍!")
            print("배고픔 정도: ", self.hungry)
        
        else:
            print("밥 좀 먹고 산책합시다. 멍멍!")
            print("배고픔 정도: ", self.hungry)

    def shampoo(self):
        print("목욕 끝! 깨끗해졌어요.")


puppy = input("강아지 이름을 지어주세요: ")

game = Dog(puppy, "brown")
text=f"당신의 강아지 이름은 {puppy}이고, 브라운 푸들입니다.\n 명령어를 실행해주세요.\n- 밥 먹기: eat\n - 산책하기: walk\n - 목욕하기: shampoo\n"

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)  # 0.1초의 간격으로 한 글자씩 출력

for util in range(10):
    util = input("기능: ")
    
    if util == "eat":
        game.eat()
    elif util == "walk":
        game.walk()
    elif util == "shampoo":
        game.shampoo()
    else:
        print("제공하지 않는 기능입니다.")
