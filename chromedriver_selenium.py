import os
from selenium import webdriver
from bs4 import BeautifulSoup

# ChoromeDriver 경로 설정 및 실행
print(os.getcwd())    # 현재 경로
driver = webdriver.Chrome('/Users/YB/Downloads/chromedriver')
driver.implicitly_wait(3)

# URL 접속 후 python 검색
driver.get('https://google.com')
driver.find_element_by_name("q").send_keys('python')
driver.find_element_by_name('btnK').click()

driver.implicitly_wait(3)
htmls = driver.page_source
soup = BeautifulSoup(htmls, 'html.parser')
python_name = soup.select('div.yuRUbf > a > h3 > span')

# 출력하기
for n in python_name:
    print(n.text.strip())
