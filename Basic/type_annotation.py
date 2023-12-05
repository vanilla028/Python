# 타입 어노테이션(annotation)
# num: int = 1

def mul(a: int, b: int) -> int:
    return a*b

print(mul(3, 5)) # 15

# 어노테이션 타입:
# int, str, list, tuple, dict, set, bool
# mypy로 Python 정적 타입 검사를 할 수 있다.
# mypy filename.py
