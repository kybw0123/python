import os
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime

# ChoromeDriver 경로 설정 및 실행

print(os.getcwd())
driver = webdriver.Chrome('C:/Users\kybw0\Downloads\chromedriver_win32/chromedriver')
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
    Google_Play_Game = open('Google_Play_Game.txt','a')



    if i == 0 :
        nowDate = datetime.datetime.now()
        Google_Play_Game.write(nowDate.strftime('%Y-%m-%d'))
        Google_Play_Game.write('\n------인기 앱/게임------\n')
    elif i == 10:
        Google_Play_Game.write('\n------인기 유료 게임------\n')
    elif i == 20:
        Google_Play_Game.write('\n------최고 매출 게임------\n')


    if i < 10 :
        Google_Play_Game.write(str(i+1) + '위' + '\n')
    elif i < 20 :
        Google_Play_Game.write(str(i-9) + '위' + '\n')
    elif i < 30 :
        Google_Play_Game.write(str(i-19) + '위' + '\n')


    Google_Play_Game.write('게임명 : ' + name_result[i] + '\n')
    Google_Play_Game.write('회사명 : ' + company_result[i] + '\n')
    Google_Play_Game.write('\n')

    i = i + 1
    Google_Play_Game.close()
