# 텍스트를 음성으로 변환하기
from gtts import gTTS
import playsound
import os

# 텍스트 입력하고 mp3 출력
text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"hi.mp3")

playsound.playsound("hi.mp3")

# 텍스트 파일을 가지고 와서 저장 후 읽기
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'text.txt'
with open(file_path, 'rt', encoding='UTF-8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save(r"myText.mp3")

playsound.playsound("myText.mp3")