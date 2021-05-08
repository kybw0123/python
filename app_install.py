from appium import webdriver
import time
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
    "browserName": "Chrome"
}
path = os.getcwd()
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(100)
print('wait100')
driver.get('https://www.naver.com')
driver.save_screenshot(filename='naver1.png')
print('naver 접속')
driver.implicitly_wait(1000)
driver.find_element_by_css_selector('#MM_SEARCH_TUTORIAL_LAYER > div > button').click()
print('close')
driver.implicitly_wait(100)
driver.find_element_by_css_selector('#MM_SEARCH_COUCH_MARK_LAYER > div > button').click()
print('close2')
driver.find_element_by_css_selector('#MM_SEARCH_FAKE').click()
driver.find_element_by_css_selector('#query').send_keys('네이버 검색')
driver.find_element_by_css_selector('#sch_w > div > form > button').click()
time.sleep(2)
driver.save_screenshot('naver2.png')
print('검색')

driver.close()