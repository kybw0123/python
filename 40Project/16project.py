import imaplib
import email
import time
from email import policy

# 네이버 이메일을 읽는 코드

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'kybw0123'
pw = '비밀번호'
imap.login(id,pw)

imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-5:] # 5개의 최신 메일 읽기 -5의 값을 변경하면 메일수 변경

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)
    print('='*70)
    print('FROM:', email_message['From'])
    print('SENDER:', email_message['Sender'])
    print('TO:', email_message['To'])
    print('DATE:', email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('SUBJECT:', subject)
    print('='*70)

#imap.close()
#imap.logout()



# 이메일 본문 내용을 읽는 코드 만들기

# 1~20 앞에 부분 위에꺼 사용

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    print('='*70)
    print('FROM:', email_message['From'])
    print('SENDER:', email_message['Sender'])
    print('TO:', email_message['To'])
    print('DATE:', email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('SUBJECT:', subject)

    print('[CONTENT]')
    message = ''
    if email_message.is_multipart():
        for part in email_message.get_payload():
            if part.get_content_type() == 'text/plain':
                bytes = part.get_payload(decode=True)
                encode = part.get_content_charset()
                message = message + str(bytes, encode)
    print(message)
    print('='*70)

#imap.close()
#imap.logout()

# 특정 키워드의 이메일을 받으면 슬랙으로 메시지 보내는 코드 만들기
import requests
import json

slack_webhook_url = 'https://hooks.slack.com/services/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'

def sendSlackWebhook(strText):
    headers = {
        'Content-type': 'application/json'
    }

    data = {
        'text':strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return 'ok'
    else:
        return 'error'

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    email_from = str(email_message['From'])
    email_date = str(email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    subject_str = str(subject)
    if subject_str.find('로그인') >= 0:
        slack_send_message = email_from + '\n' + email_date + '\n' + subject_str
        sendSlackWebhook(slack_send_message)
        print(slack_send_message)

#imap.close()
#imap.logout()


# 반복 실행하여 새로운 이메일이 있을 경우에만 메시지 보내는 코드 만들기

send_list = []

while True:
    try:
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()
        last_email = all_email[-100:]

        for mail in reversed(last_email):
            result, data = imap.uid('fetch', mail, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email, policy=policy.default)

            email_from = str(email_message['From'])
            email_date = str(email_message['Date'])
            subject, encode = find_encoding_info(email_message['Subject'])
            subject_str = str(subject)
            if subject_str.find('로그인') >= 0:
                slack_send_message = email_from + '\n' + email_date + '\n' + subject_str
                if slack_send_message not in send_list:
                    sendSlackWebhook(slack_send_message)
                    print(slack_send_message)
                    send_list.append(slack_send_message)

            time.sleep(30)
    except KeyboardInterrupt:
        break

imap.close()
imap.logout()