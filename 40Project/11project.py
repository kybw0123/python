import time

import pyautogui
import os

# 사진에서 좌표 추출하는 코드 만들기
# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
import pyperclip

os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('original_1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('original_2.png')
    print(picPosition)
if picPosition is None:
    picPosition = pyautogui.locateOnScreen('original_3.png')
    print(picPosition)
#Box(left=1006, top=918, width=246, height=142)

# 좌표를 이용하여 메시지를 자동으로 보내는 코드 만들기
clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)
time.sleep(1)

pyperclip.copy('이 메시지는 자동으로 보내는 메세지 입니다.')
pyautogui.hotkey("command","v")
time.sleep(1)

# 진짜 pyautogui는 좌표 제대로 못불러오는것 같음...그러므로 난 그냥 포기하겠다
