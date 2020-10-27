import os
from selenium import webdriver
from bs4 import BeautifulSoup

# ChoromeDriver 경로 설정 및 실행
print(os.getcwd())    # 현재 경로
driver = webdriver.Chrome('/Users/YB/Downloads/chromedriver')
driver.implicitly_wait(3)

# URL 접속 후 python 검색
driver.get('https://google.com')
driver.find_element_by_name("q").send_keys('트럼프')
driver.find_element_by_name('btnK').click()

driver.implicitly_wait(3)
htmls = driver.page_source
soup = BeautifulSoup(htmls, 'html.parser')
python_name = soup.select('#result-stats')
# 출력하기
for n in python_name:
    print('트럼프')
    print(n.text.strip())

# 검색어 삭제 후 새로운 검색
driver.find_element_by_name("q").clear()
driver.find_element_by_name('q').send_keys('바이든')
driver.find_element_by_class_name('Tg7LZd').click()

driver.implicitly_wait(3)
htmls2 = driver.page_source
soup2 = BeautifulSoup(htmls2, 'html.parser')
python_name2 = soup2.select('#result-stats')

# 출력하기
for n in python_name2:
    print('바이든')
    print(n.text.strip())
