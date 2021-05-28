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
# 172.30.1.36:5555

desired_caps = {
    "platformName": "Android",
    "deviceName": "LMG820Nfa62cee2"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
actions = TouchAction(driver)

# 앱 실행
driver.start_activity("com.ingka.ikea.app", "com.ingka.ikea.app.SplashActivity")
time.sleep(3)


# 검색창에 책상 검색하기
driver.find_element_by_class_name('android.widget.EditText').click()
driver.find_element_by_class_name('android.widget.EditText').send_keys('책상')
driver.press_keycode(66)
time.sleep(2)


# 검색 결과중 첫번째 상품 선택
print(driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[2]").text)
driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"제품\"])[1]").click()


# 안드로이드 키 코드에 대한 숫자값
# https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_ENTER


driver.close_app()
