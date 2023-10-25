# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까?
# 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

s = "Calm Peace peace autumn Autumn quiet generous love sky cloud Sky wind Sky"

s = s.lower()
words = s.split()

# 중복 제외 단어 수
unique_words = set(words)
print(unique_words) # {'cloud', 'peace', 'love', 'wind', 'autumn', 'generous', 'sky', 'calm', 'quiet'}

# 단어 수
print(len(unique_words)) # 9


result = {}


for word in words:
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1

# 단어 수
print(len(result.keys())) # 9
print(result) # {'calm': 1, 'peace': 2, 'autumn': 2, 'quiet': 1, 'generous': 1, 'love': 1, 'sky': 3, 'cloud': 1, 'wind': 1}