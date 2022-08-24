import socket

# 내부 ip 알아보기
# 내 컴터에서는 안되는듯
in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)

# 컴퓨터의 외부 및 내부 IP 확인
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓을 연결하기
in_addr.connect(("www.google.co.kr", 443))  # 구글에 접속하고 접속 포트는 443
print("내부 IP :",in_addr.getsockname()[0]) # 연결된 소켓의 이름 출력


# 컴퓨터의 외부 및 내부 IP 확인
# 필요한 모듈 부르기
import requests
import re

req = requests.get("http://ipconfig.kr") # 사이트 접속

#정규식 표현을 사용하여 ip주소를 가져와 저장
out_addr = re.search(r"IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",req.text)[1]

print("외부 IP :",out_addr)
