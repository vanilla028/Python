import random
random_number = random.randint(1, 100)

#print(random_number)
game_count = 1

while True:
    my_number = int(input('1-100 사이의 숫자를 입력하세요.'))
    if my_number > random_number:
        print("Down!")
    elif my_number < random_number:
        print("up!")
    else:
        print(f"Congratulations! {game_count}번 만에 맞추셨습니다")
#f == format 함수. 포매팅시킨다(문자열포매팅) 
        break
    game_count = game_count + 1