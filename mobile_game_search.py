import os
from selenium import webdriver
from bs4 import BeautifulSoup

# ChoromeDriver 경로 설정 및 실행
print(os.getcwd())
driver = webdriver.Chrome('/Users/YB/Downloads/chromedriver')
driver.implicitly_wait(3)

# URL 접속
driver.get('https://play.google.com/store/apps/top/category/GAME?hl=ko')
driver.implicitly_wait(3)

# 페이지 소스 받아서 인기 게임 이름 출력하기
soup = BeautifulSoup(driver.page_source, 'lxml')

i = 0
# 게임명, 회사명 리스트로 저장할 준비
name_result =[]
company_result = []
name = soup.findAll('div', attrs={'class':'k6AFYd'})
company = soup.findAll(attrs={'class': 'b8cIId ReQCgd KoLSrc'})

# for문을 이용해서 미리 변수에 값 저장
for data in name:
    name_result.append(data.a.text)

for data2 in company:
    company_result.append(data2.a.text)

# 출력하기
while i < len(name_result):
    if i == 0 :
        print('------인기 앱/게임------')
    elif i == 10:
        print('')
        print('------인기 유료 게임------')
    elif i == 20:
        print('')
        print('------최고 매출 게임------')

    print('게임명 : ' + name_result[i])
    print('회사명 : ' + company_result[i])
    print('')

    i = i + 1