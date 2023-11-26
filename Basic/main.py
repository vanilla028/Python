import sys

print(sys.path)
['C:\\Users\\해피마미\\connected_github\\Python\\Basic', 'C:\\Users\\miniconda3\\envs\\practice\\python38.zip', 'C:\\Users\\miniconda3\\envs\\practice\\DLLs', 'C:\\Users\\miniconda3\\envs\\practice\\lib', 'C:\\Users\\miniconda3\\envs\\practice', 'C:\\Users\\miniconda3\\envs\\practice\\lib\\site-packages', 'C:\\Users\\miniconda3\\envs\\practice\\lib\\site-packages\\win32', 'C:\\Users\\miniconda3\\envs\\practice\\lib\\site-packages\\win32\\lib', 'C:\\Users\\miniconda3\\envs\\practice\\lib\\site-packages\\Pythonwin']

# 만약 임포트한 module.py가 다른 경로에 있는 경우 추가한다.
sys.path.append('C:\\Users\\해피마미')

# 또는 명령프롬프트에서 다음을 설정
# set PYTHONPATH=C:\Users\해피마미


import module
result = module.add(4000, 500)
print(result)

