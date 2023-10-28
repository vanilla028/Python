# 45분 일찍 알람 설정하기

h, m = map(int, input("알람 시간 설정: ").split())
total = h * 60 + m - 45
h = total // 60
m = total % 60

print(f"알람 설정 시간: {h}:{m}")
