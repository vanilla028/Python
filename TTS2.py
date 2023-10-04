from gtts import gTTS
text =  "긴급 속보입니다. 해피가 '아빠, 보고 싶어요'라고 하며 드디어 말문을 열었습니다. 얼른 데리러 오세요."

tts = gTTS(text=text, lang='ko')
tts.save(r"./hello2.mp3")