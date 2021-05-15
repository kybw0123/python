from appium import webdriver
import time
import os
from appium.webdriver.common.touch_action import TouchAction


# 실행시킬 안드로이드 정보 입력하기
# platformName = iOS, Android or FirefoxOS 모바일 OS 플래폼 등 정보
# automationName = Appium(default), UiAutomator2, Espresso 등 자동화 엔진 정보
# platformVersion = 7,8,9,10 모바일 OS 버전
# deviceName = 디바이스 이름 찾아서 추가
# app = 앱 설치 경로
# otherApps  = 여러앱을 리스트나 JSON으로 설치하는 경로를 추가한다
# browserName = 자동화 할 모바일 웹 브라우저의 이름입니다. Safari, Chrome, Chromium 등
# noReset = true, false 테스트 후 해당 상태를 초기화 하는 기능 true면 초기화 하지 않음
# LMG820Nfa62cee2

desired_caps = {
    "platformName": "Android",
    "deviceName": "LMG820Nfa62cee2",
    "app": "/Users/YB/Downloads/python_git/python/IKEA_v2.25.0_apkpure.com.apk",
    "noReset": "False"
}
path = os.getcwd()
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
actions = TouchAction(driver)
driver.implicitly_wait(1000)
driver.save_screenshot('IKEA_START.png')
driver.find_element_by_class_name('android.widget.ImageButton').click()

# A 좌표에서 B 좌표까지 터치한 상태에서 이동하기

time.sleep(2)
driver.save_screenshot('IKEA_move_before.png')
actions.long_press(x=689,y=2605).move_to(x=720,y=313).release().perform()
actions.long_press(x=700,y=2605).move_to(x=720,y=303).release().perform()
actions.long_press(x=700,y=2605).move_to(x=720,y=303).release().perform()
driver.save_screenshot('IKEA_move_after.png')

driver.find_element_by_class_name('android.widget.ImageButton').click()

# 앱 로딩시간 때문에 대기
time.sleep(7)

# 검색창에 책상 검색하기
driver.save_screenshot('IKEA_search.png')
driver.find_element_by_class_name('android.widget.EditText').click()
driver.find_element_by_class_name('android.widget.EditText').send_keys('책상')
driver.press_keycode(66)
time.sleep(2)
driver.save_screenshot('IKEA_serach_info.png')

driver.implicitly_wait(1000)

# 안드로이드 키 코드에 대한 숫자값
# https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_ENTER


driver.close_app()
