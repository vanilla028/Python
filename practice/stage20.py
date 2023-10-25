# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

s = "aronamjkmjmjmj"
dic = {}

# 각 알파벡에 대해 초기값을 -1로 설정
for letter in 'abcdefghijklmnopqrstuvwxyz':
    dic[letter] = -1

# 알파벳의 첫 등장 위치를 저장
for i, alphabet in enumerate(s):
    if dic[alphabet] == -1:
        dic[alphabet] = 1
    else:
        dic[alphabet] += 1   

print(dic)
print(dic.values())

"""
{'a': 2, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': 4, 'k': 1, 'l': -1, 
'm': 4, 'n': 1, 'o': 1, 'p': -1, 'q': -1, 'r': 1, 's': -1, 't': -1, 'u': -1, 'v': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1}

dict_values([2, -1, -1, -1, -1, -1, -1, -1, -1, 4, 1, -1, 4, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1])
"""