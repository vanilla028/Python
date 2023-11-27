# 직접 예외 만들기
class MyError(Exception): # 파이썬 내장 클래스인 Exception 클래스 상속
    def __str__(self):
        return "허용되지 않는 닉네임입니다."

def nickname(nick):
    if nick in ['똥개', '말미잘', '멍텅구리']:
        raise MyError()
    print(nick)

try:
    nickname('천재')
    nickname('똥개')

except MyError as e:
    print(e)


"""
파이썬 내장 예외 출력시:

def nickname(nick):
    if nick in ['똥개', '말미잘', '멍텅구리']:
        raise ValueError("허용되지 않는 닉네임입니다.")
"""
