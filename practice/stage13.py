# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

try:
    a = list(map(int, input("정수 N개를 차례로 입력하세요(공백으로 분리): ").split()))
    if a:
        print(f"리스트에서 최솟값은 {min(a)}, 최댓값은 {max(a)}입니다.")
    else:
        print("입력된 정수가 없습니다.")

except ValueError:
    print("올바른 정수를 입력하세요.")


# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

num = list(map(int, input("자연수 9개를 입력하세요: ").split()))
max_value = max(num)
max_index = num.index(max_value)

print(f"최댓값은 {max_value}이고, 리스트에서 {max_index+1}번째 수입니다.")
