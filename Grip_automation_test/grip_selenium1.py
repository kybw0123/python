import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)

# 그립 접속
driver.get('https://grip.show/discover')
driver.implicitly_wait(1000)
#time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'#root > div > div.root-layout.null.MuiBox-root.css-1l4w6pd > main > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > ul > li.type_25 > div > div > div:nth-child(1) > div:nth-child(1) > img').click()
driver.find_element(By.CSS_SELECTOR,'#root > div > div.root-layout.null.MuiBox-root.css-1l4w6pd > main > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > ul > li.type_25 > div > div > div:nth-child(1) > div:nth-child(2) > img').click()
driver.implicitly_wait(1000)
driver.find_element(By.CSS_SELECTOR,'#root > div > div.root-layout.null.MuiBox-root.css-1l4w6pd > main > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > header > div > div.MuiTabs-root.css-teesge > div.MuiTabs-scroller.MuiTabs-hideScrollbar.MuiTabs-scrollableX.css-12qnib > div > button:nth-child(3)').click()

#root > div > div.root-layout.null.MuiBox-root.css-1l4w6pd > main > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > header > div > div.MuiTabs-root.css-teesge > div.MuiTabs-scroller.MuiTabs-hideScrollbar.MuiTabs-scrollableX.css-12qnib > div > button:nth-child(2)
#root > div > div.root-layout.null.MuiBox-root.css-1l4w6pd > main > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > header > div > div.MuiTabs-root.css-teesge > div.MuiTabs-scroller.MuiTabs-hideScrollbar.MuiTabs-scrollableX.css-12qnib > div > button:nth-child(3)
#root > div > div.root-layout.null.MuiBox-root.css-1l4w6pd > main > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > header > div > div.MuiTabs-root.css-teesge > div.MuiTabs-scroller.MuiTabs-hideScrollbar.MuiTabs-scrollableX.css-12qnib > div > button:nth-child(4)
#driver.close()
