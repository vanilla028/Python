# 45분 일찍 알람 설정하기
h, m = map(int, input().split())
if m < 45:
    m = m + 15
    print(h - 1,":", m)
else:
    m = 45 - m
    print(h, ":", m)