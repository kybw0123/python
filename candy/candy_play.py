import unittest
import os
import datetime
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import cv2
import numpy as np


# Set up appium
# Appium 서버는 로컬로 설정
# 디바이스 정보는 G8로 넣습니다.
# 실행앱의 위치 지정
# 앱피온 설정
# "app": "파일경로"를 하면 앱이 설치 된다.
# "appPackage" : "패키지ID"
# "appActivity" : "실행이름"
# 패키지랑 액티비티를 이용하면 설치하지 않고 기존 앱을 실행할 수 있다.


# appium실행 정보
desired_capbilities = {
    "platformName": "Android",
    "deviceName": "LMG820Nfa62cee2",
    "app": "/Users/YB/Downloads/python_git/python/candy/Candy Crush Saga_v1.207.0.2_apkpure.com.apk",
    "noReset": True
}

# 이미지파일 리스트로 저장
image_path = "/Users/YB/Downloads/python_git/python/candy/search_image"
file_list = os.listdir(image_path)
images = []
for i in range(len(file_list)):
    file_name, file_extension = os.path.splitext(file_list[i])
    images.append(file_name)
images.sort()



# cv2를 이용하여 이미지 찾고 좌표 정하기
class Matching():

    def detectimage(self, screenshotPath, detectImagePath):

        sourceimage = cv2.imread(screenshotPath, 0)
        template = cv2.imread(detectImagePath, 0)

        w, h = template.shape[::-1]

        # TM_CCOEFF_NORMED 방식으로 매칭
        method = eval('cv2.TM_CCOEFF_NORMED')
        res = cv2.matchTemplate(sourceimage, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # 이미지 전체 크기 확인 좌측상단, 우측하단, 중앙
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = (top_left[0] + int(w / 2), top_left[1] + int(h / 2))

        # 색깔 설정
        color = (0,0,255)
        # 이미지, 좌측상단, 우측하단, 색깔, 굵기
        cv2.rectangle(sourceimage, top_left, bottom_right, color, thickness=8)

        detectImagePath = screenshotPath[:-6] + '-detect.png'
        cv2.imwrite(detectImagePath, sourceimage)

        return center


class Candy(unittest.TestCase):
# 현재시간 출력
    def makeTS(self):
        return str(int(datetime.datetime.now().timestamp()))

    def strDatetime(self):
        return str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
# 앱피움 실행하기
    def setUp(self):
        # print("설치 완료")
        # Set up appium
        # 그리고 desired_capbilities에 연결하려는 디바이스의 정보를 넣습니다.
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capbilities)
        print("실행")

# 테스트 케이스 설정
    def test_search_field(self):

        sleep(18)
        print("시작후 18초 대기")

        matching = Matching()

        # 스크린샷을 저장할 폴더를 생성합니다.
        test_folder_name = self.strDatetime()
        currentPath = '%s/' % os.getcwd()
        test_Directory = currentPath + test_folder_name + '/'
        searchimages = 'search_image/'  # 이미지 찾을 폴더
        print("현재 위치")
        print(currentPath)
        print("폴더 이름")
        print(test_folder_name)

        if not os.path.exists(test_Directory):
            os.makedirs(test_Directory)

            driver = self.driver
            wait = WebDriverWait(driver, 20)

            sleep(17)
            print("2")

        def Search_Image_Touch(y):
            screenshotPath = test_Directory + '%s-screenshot.png' % self.makeTS()
            detectImagePath = currentPath + searchimages + y + '.png'
            driver.save_screenshot(screenshotPath)
            center = matching.detectimage(screenshotPath, detectImagePath)
            sleep(3)
            driver.tap([center])
            sleep(1)
            print(y + ' 터치')


        x = 0
        while x < len(images):
            # 마지막 사진 나왔을때 대기 3초
            if x == len(images):
                sleep(3)
                #driver.reset()
                driver.close_app()
                sleep(1)
                driver.remove_app('com.king.candycrushsaga')
                print("끝")
            else:
                Search_Image_Touch(images[x])
            x = x + 1


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Candy)
    unittest.TextTestRunner(verbosity=2).run(suite)