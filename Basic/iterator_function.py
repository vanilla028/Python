# 이터레이터(iterator)

num_list = [2, 4, 6, 8, 10]
iterator = iter(num_list) # 리스트를 이터레이터로 변경
print(type(iterator)) # <class 'list_iterator'>

print(next(iterator)) # 2
print(next(iterator)) # 4
print(next(iterator)) # 6
print(next(iterator)) # 8
print(next(iterator)) # 10
# print(next(iterator)) # StopIteration 예외 발생

# 이터레이터의 값을 가져오는 일반적인 방법
# for문을 사용하면 StopIteration 예외가 발생하지 않는다.
# 만약 위의 next() 함수를 사용하여 이미 반복하였다면 아래 for문에서는 동작하지 않는다.
for i in iterator:
    print(i)



