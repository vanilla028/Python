# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

a, b, c = map(int, input().split())
d = (a+b)%c
e =  ((a%d) + (b%c))%c
f = (a*b)%c
g = ((a%c)*(b%c))%c

if d == e:
    print("(A+B)%C는 ((A%C) + (B%C))%C 와 같다.")
else:
    print("(A+B)%C는 ((A%C) + (B%C))%C 와 같지 않다.")

if f == g:
    print("(A×B)%C는 ((A%C) × (B%C))%C 와 같다.")
else:
    print("(A×B)%C는 ((A%C) × (B%C))%C 와 같지 않다.")

"""
5 7 10
(A+B)%C는 ((A%C) + (B%C))%C 와 같지 않다.
(A×B)%C는 ((A%C) × (B%C))%C 와 같다.
"""
