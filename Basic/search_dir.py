# 디렉토리 검색하기
import os

def search(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        total = os.path.join(dir, filename)
        print(total)


search("./")
"""
./practice1.py
./hello.py
"""

# 파이썬 파일만 검색하려면?
# 현재 디렉토리에서 검색하기

def search_py1(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        info = os.path.join(dir, filename)
        temp = os.path.splitext(info)[-1]
        if temp == ".py":
            print(info)

search_py1("./")

# 하위 디렉토리까지 검색하려면?
def search_py2(dir):
    try:
        filenames = os.listdir(dir)
        for filename in filenames:
            info = os.path.join(dir, filename)
            if os.path.isdir(info):
                search(info)
            else:
                temp = os.path.splitext(info)[-1]
                if temp == ".py":
                    print(info)
    except PermissionError:
        print("Error: 접근 오류 발생")

search_py2("./")





