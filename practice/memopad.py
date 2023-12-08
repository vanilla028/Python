# 메모를 파일에 저장하고 추가 및 조회가 가능한 메모자을 만들어 보자.
import sys

# python memopad.py -put "Hello, World!"
# python memopad.py -put "I am Arona."
# python memopad.py -print

user = sys.argv[1]

if user == '-put':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif user == '-print':
    f = open('memo.txt', 'r')
    contents = f.read()
    print(contents)
    f.close()
    # Hello, World!
    # I am Arona.



