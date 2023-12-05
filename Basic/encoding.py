# 문자열 인코딩

sentence = "Hello, I am Arona"
encoded_sentence = sentence.encode('utf-8')
print(encoded_sentence)
# b'Hello, I am Arona'
# 'b'는 바이트 문자열을 나타내기 위해 사용되는 표시
# 실제 데이터에는 영향을 미치지 않는다.

print(type(encoded_sentence))
# <class 'bytes'>

# 문자열 디코딩
decoded_sentence = encoded_sentence.decode('utf-8')
print(decoded_sentence) # Hello, I am Arona
print(type(decoded_sentence)) # <class 'str'>

