import os
import shutil
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
import requests



def chromedriver_update():
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]    # 현재 크롬 버전 확인 및 뒷버전 구분
    current_list = os.listdir(os.getcwd())    # 현재폴더 목록
    chrome_list = []    # 크롬 버전 추가할 빈 변수
    for i in current_list:
        path = os.path.join(os.getcwd(),i)    # 현재 경로의 모든객체의 전체 경로
        if os.path.isdir(path):    # 그 경로가 폴더인지 확인
            if 'chromedriver' in os.listdir(path):    # 폴더면 안에 chromedriver이 있는지 확인(mac용)
                chrome_list.append(i)    # 있으면 비어있는 변수에 추가

    old_version = list(set(chrome_list)-set([chrome_ver]))    # 그중에 최신버전은 제외

    for i in old_version:
        path = os.path.join(os.getcwd(),i)    # 구버전이 있는 폴더의 경로
        shutil.rmtree((path))    # 그 경로 삭제

    if not chrome_ver in current_list:    # 최신버전 폴더가 현재 경로에 없으면
        chromedriver_autoinstaller.install(True)    # 크롬드라이버 설치
    else: pass    # 아니면 무시

    return os.getcwd() +'/' + chrome_ver + '/chromedriver'    # 크롬드라이버 경로 보내주기







if __name__ == '__main__':
    chrome_path = chromedriver_update()
    #print(chrome_path)
    driver = webdriver.Chrome(chrome_path)
    driver.get('https://developer.apple.com/kr/news/')
    driver.implicitly_wait(100)
    html = driver.page_source
    response = requests.get('https://developer.apple.com/kr/news/')
    data = response.text
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('#article-v868vy6e > section > section')

    soup2 = BeautifulSoup(data, 'lxml')
    tags = soup2.find_all('a')
    news_url = []

    for tag in tags:
        a = tag.get('href')
        b = str(a)
#        print(b[:3])

        if b[:3] == 'htt':
            news_url.append(b)




    a = soup.select('#article-v868vy6e > section > section > div > span > p:nth-child(3) > a')
#    print(a)
    for n in notices:
         print(n.text.strip())

    driver.quit()

