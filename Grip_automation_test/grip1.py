import time
from appium import webdriver
import os

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
    "deviceName": "LMG820Nfa62cee2",
    "app": "/Users/YB/Downloads/그립 Grip 전국민 라이브 大장터_v2.23.2_apkpure.com.apk",
    "noReset": "True"
}

path = os.getcwd()
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(1000)
driver.save_screenshot('Grip_START.png')
time.sleep(2)
driver.close_app()
driver.remove_app('show.grip')
driver.quit()