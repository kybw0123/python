import os
from selenium import webdriver
from bs4 import BeautifulSoup

# ChoromeDriver 경로 설정 및 실행
print(os.getcwd())
driver = webdriver.Chrome('/Users/YB/Downloads/chromedriver')
driver.implicitly_wait(3)

# URL 접속
driver.get('http://www.gevolution.co.kr/rank/aos')
driver.implicitly_wait(3)
'''
# 페이지 소스 받아서 인기 게임 이름 출력하기
soup = BeautifulSoup(driver.page_source, 'lxml')
#print(soup)
i = 1
for data in soup.findAll(name="span", attrs={'class':'rank1', 'alt':'개발사 정보'} ):
    print(str(i) + '위 : '+data.text.strip())
    i += 1
'''