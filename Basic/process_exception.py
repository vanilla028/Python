# 예외처리 하는 법
try:
    a, b = map(int, input("숫자 두 개를 입력하세요: ").split())
    result = a / b
    print(result)
except:
    print("Error!")

# 오류 내용 확인하기 - 발생 오류와 오류 변수까지 포함한 except문
try:
    a, b = map(int, input("숫자 두 개를 입력하세요: ").split())
    result = a / b
    print(result)  
except ZeroDivisionError as e:
        print("Error: 나누기 연산 중 오류 발생 -", e) # division by zero
except ValueError:
    print("Error: 올바른 숫자를 입력하세요.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
except Exception as e:
    print("Error: 알 수 없는 오류 발생 -", e)

"""
다음과 같이 함께 처리할 수도 있다.
except (ZeroDivisionError, IndexError) as e:
    print(e)
"""


# try-filnally문
try:
    f = open('aaa.txt', 'w')
    data = '안녕하세요!\n저는 인공지능을 공부하는 학생입니다.'
    f.write(data)
finally:
    f.close() # 오류 발생시에도 무조건 실행된다.

# try-else문
try:
    a, b = map(int, input("나눗셈을 할 숫자 두 개를 입력하세요: ").split())
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print(e)
else: # 오류가 없을 경우에만 수행
    print("더하기를 수행합니다. 값은: {}" .format(a+b))


# 오류 회피하기
try:
    f = open("no", 'r')
except FileNotFoundError:
    pass
    