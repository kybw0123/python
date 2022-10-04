import telegram

# api token을 이용하여 bot의 id를 알아내는 코드 만들기
# 봇 생성 후 딜레이가 있어 바로 하면 오류가 발생할 수 있음
token = '5455163486:AAEusybxyqnLYNhaOw-EsuqDLyhuTSBUlj4'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
print(bot)
for u in updates:
    print(u)
# id 알아내고 메시지 보내기

id = '509395581'
bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")

# 텔레그램 bot 기능을 활용하여 메시지의 자동응답 보내는 코드 만들기
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if user_text == "안녕":
        bot.sendMessage(id,text="어 그래 안녕")
    elif user_text =="뭐해":
        bot.sendMessage(id,text="그냥 있어")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)