# list
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]


# a와 b의 교집합 구하기
c = []

for i in a:
    if i in b:
        c.append(i)

print(c) # [3, 4, 5]

# a와 b의 합집합 구하기

print(set(a+b))

d = []

for i in a:
    d.append(i)

for i in b:
    d.append(i)

print(set(d))

# 리스트 a에 인덱스 0에 100 넣기
a.insert(0, 100)
print(a) # [100, 1, 2, 3, 4, 5]

# a의 인덱스 0 반환
print(a.index(100))

# 리스트 a에서 3번째 인덱스 삭제
del a[2]
print(a) # [1, 2, 4, 5]

# 리스트 d에서 첫번째로 나오는 5 삭제
d.remove(5)
print(d) # [1, 2, 3, 4, 3, 4, 5, 6, 7]

# 리스트 d에서 0번째 인덱스 삭제 및 리턴
print(d.pop(0))
print(d) # [2, 3, 4, 3, 4, 5, 6, 7]

# 본체 리스트 변환X 오름차순, 내림차순 정렬 반환하기
print(sorted(d))
print(sorted(d, reverse=True))
print(d)
# 리스트 d 오름차순, 내림차순 정렬
d.sort()
print(d) # [2, 3, 3, 4, 4, 5, 6, 7]

d. sort(reverse=True)
print(d) # [7, 6, 5, 4, 4, 3, 3, 2]

d.sort()
print(d) # [2, 3, 3, 4, 4, 5, 6, 7]

d.reverse()
print(d) # [7, 6, 5, 4, 4, 3, 3, 2]


