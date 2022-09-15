import pyautogui
import time
import pyperclip

#  # 마우스의 좌표를 출력하는 코드 만들기
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)


# # 네이버에서 자동으로 서울 날씨 검색하는 코드 만들기
# pyautogui.moveTo(1015,274,0.2)
# pyautogui.click()
# time.sleep(0.5)
#
# pyperclip.copy("서울 날씨")
# pyautogui.hotkey("command", "v")   # 아~ 나 맥이였음
# time.sleep(0.5)
#
# pyautogui.write(['enter'])
# time.sleep(1)

# 날시 검색 후 자동 캡처 후 저장하는 코드 만들기
# 좌표대로 해도 안되네 개떡같네 진짜
start_x = 664
start_y = 294
end_x = 1407
end_y = 740

#pyautogui.screenshot(r'서울날씨.png',region=(end_x-50, end_y-200, end_x, end_y+200))


# 여러 지역 날씨를 자동으로 검색 후 저장하는 코드 만들기
weather = ['서울 날씨', '시흥 날씨', '청주 날씨', '부산 날씨', '속초 날씨', '강원도 날씨']
addr_x = 249
addr_y = 88

for country_weather in weather:
    pyautogui.moveTo(addr_x,addr_y,1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com",interval = 0.1)
    pyautogui.write(['enter'])
    time.sleep(1)

    pyperclip.copy(country_weather)
    pyautogui.hotkey("command", "v")  # 아~ 나 맥이였음
    time.sleep(0.5)
    pyautogui.write(['enter'])
    time.sleep(1)
    save_path = country_weather + '.png'
    pyautogui.screenshot(save_path, region=(end_x - 50, end_y - 200, end_x, end_y + 200))
