# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

qr_code_alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"
t = int(input("테스트 케이스의 개수를 입력하세요: "))

results = []
for _ in range(t):
    r, s = map(str, input("반복할 횟수와 문자열을 입력하세요(공백 분리): ").split())
    new = ""
    for i in s:
        new += i * int(r)
    results.append(new)


for result in results:
    print(result)
 
"""
테스트 케이스의 개수를 입력하세요: 2
반복할 횟수와 문자열을 입력하세요(공백 분리): 2 012
반복할 횟수와 문자열을 입력하세요(공백 분리): 2 CDE
001122
CCDDEE
 """