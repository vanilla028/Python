import pandas as pd
import random
from gtts import gTTS

# 파일 읽어오기
interview = pd.read_excel("interview_by_mj.xlsx")
"""
파일은 다음과 같은 형태로 되어 있다.
AI  지도 학습과 비지도 학습에 대해 설명하시오.  지도 학습은 레이블이 있는...
"""

q = interview.iloc[:, 1]

# 무작위로 하나의 행 선택하기
selected_q = q.sample(n=1, random_state=random.seed()).values[0]

tts = gTTS(text=selected_q, lang='ko')
tts.save("random_question.mp3")