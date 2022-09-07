from currency_converter import CurrencyConverter

# 통화 목록 출력하기
cc = CurrencyConverter()
print(cc.currencies)

# 1달러를 원화로 변환한 결과 출력 코드 만들기
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.convert(1,'USD', 'KRW'))


# 실시간 환율 정보 크롤링 코드 만들기
import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent' : 'Mozilla/5.0',
        'Content-Type' : 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1,target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)

get_exchange_rate('usd','krw')