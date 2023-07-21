import threading
import telebot
import requests
import json
import schedule
import time

from chats_state import Chats
from enviroments import REG_RU_API_KEY, TG_BOT_API_KEY, SCHEDULE_TIME, REGION

chats = Chats()
bot = telebot.TeleBot(TG_BOT_API_KEY)


def requestToReg():
    response = requests.get('https://api.cloudvps.reg.ru/v1/balance_data', headers={
        "Authorization": REG_RU_API_KEY
    })
    data = json.loads(response.content)
    print(f'Response: {data}')

    balance = data["balance_data"]["balance"]
    days_left = data["balance_data"]["days_left"]
    monthly_cost = data["balance_data"]["monthly_cost"]

    message = f'Облачный счет составляет *{balance} ₽*\n' \
              f'Этого хватит на *{days_left} дн.*\n' \
              f'Расход средств и прогноз потребления: *{monthly_cost} ₽/месяц*'

    if len(chats.state) and days_left <= 5:
        for chat in chats.state:
            bot.send_message(chat, message, parse_mode='Markdown')


def scheduleRequest():
    print('Schedule is started')
    while True:
        schedule.run_pending()
        time.sleep(1)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Oхайо, я умею уведомлять о текущем счете на сервере. жмякни на /subscribe '
                                      'чтобы подписаться на уведомления')


@bot.message_handler(commands=['subscribe'])
def start(message):
    chats.add(message.chat.id)
    bot.send_message(message.chat.id, f'Успешно подписались! '
                                      f'\nУведомление о счете будет приходить каждый день в {SCHEDULE_TIME}, когда до '
                                      'окончания аренды сервера останется меньше *5-ти дней*.', parse_mode='Markdown')


@bot.message_handler(commands=['unsubscribe'])
def start(message):
    chats.rm(message.chat.id)
    bot.send_message(message.chat.id, 'Успешно отписались!\nЧтобы подписаться, жмякни на /subscribe')


if __name__ == "__main__":
    # Create the job in schedule.
    schedule.every().day.at(SCHEDULE_TIME, REGION).do(requestToReg)
    # Thread
    threading.Thread(target=scheduleRequest).start()
    # Bot polling
    bot.polling()
