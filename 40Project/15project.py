import requests
import json

# 봇 채널로 메시지 보내는 코드 만들기

#https://hooks.slack.com/services/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

slack_webhook_url = 'https://hooks.slack.com/services/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'

def sendSlackWebhook(strText):
    headers = {
        "Content-type":"application/json"
    }
    data = {
        "text": strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"

print(sendSlackWebhook("안녕하세요 파이썬에서 보내는 메시지 입니다."))
