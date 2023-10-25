# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# 과제를 제출한 학생 목록
submitted_students = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
students = list(range(1, 31))
print(students)
missing_students = list(set(students) - set(submitted_students))
missing_students.sort() # sorted(missing_students)로 해도 된다.
print(missing_students)

# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

number = list(map(int, input("숫자 10개를 입력하세요: ").split()))

a = []
for i in number:
    a.append(i % 42)

"""
# 리스트에 다음과 같이 요소를 추가할 수도 있다.
a = [0] * 10 # 리스트 요소를 0으로 초기화  
for i in number:
    a[i] = i% 42
"""
# print(a)
print(set(a))
print(len(set(a)))