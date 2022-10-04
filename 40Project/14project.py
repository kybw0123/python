#네이버 메일을 보내는 코드 만들기
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
'''
send_email = "kybw0123@naver.com"
send_pwd = '네이버비밀번호'

recv_email = 'kybw0123@gmail.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587

text = """
test용 이메일 발송입니다.
여러
줄을
써보겠 습니다.
^^
"""
msg = MIMEText(text)

msg['Subject'] = 'test용 메일 제목입니다.'
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()

# google 메일 보내기
send_email = "kybw0123@gmail.com"
send_pwd = "앱비밀번호"

recv_email = "kybw0123@naver.com"

smtp_name = 'smtp.gmail.com'
smtp_port = 587

text = """
test용 이메일 발송입니다.
여러
줄을
써보겠 습니다2.
^^
"""
msg = MIMEText(text)

msg['Subject'] = 'test용 메일 제목입니다.'
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()
'''

# # 파일을 첨부하여 메일 보내는 코드 만들기
# send_email = "kybw0123@gmail.com"
# send_pwd = "앱비밀번호"
#
# recv_email = "kybw0123@naver.com"
#
# smtp_name = 'smtp.gmail.com'
# smtp_port = 587
#
# msg = MIMEMultipart()
#
# msg['Subject'] = '첨부파일 test용 메일 제목입니다.'
# msg['From'] = send_email
# msg['To'] = recv_email
#
# text = """
# 첨부파일 test용 이메일 발송입니다.
# 여러
# 줄을
# 써보겠 습니다2.
# ^^
# """
#
# contentPart = MIMEText(text)
# msg.attach(contentPart)
#
# etc_file_path = r'qrcode.txt'
# with open(etc_file_path, 'rb') as f :
#     etc_part = MIMEApplication(f.read())
#     etc_part.add_header('Content-Disposition', 'attachment', filename='qrcode.txt')
#     msg.attach(etc_part)
#
#
#
# print(msg.as_string())
#
# s = smtplib.SMTP(smtp_name, smtp_port)
# s.starttls()
# s.login(send_email,send_pwd)
# s.sendmail(send_email,recv_email,msg.as_string())
# s.quit()

# html 형식 메일 보내는 코드 만들기
# 하려다가 그냥 msg를 html 코드로 적으면 됨

# 여러개 보낼때는 파일 읽고 저장하고 for문으로 반복하고 try, except로 에러시 넘어가는걸로 코드 작성하면 됨..... 사실 적기 귀찮아서 그럼