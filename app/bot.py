import telebot

from state import State
from enviroments import TG_BOT_API_KEY, SCHEDULE_TIME
from actions import reg_data_msg_action

state = State()
bot = telebot.TeleBot(TG_BOT_API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Oхайо, я умею уведомлять о текущем счете на сервере. жмякни на /subscribe '
                                      'чтобы подписаться на уведомления')


@bot.message_handler(commands=['subscribe'])
def start(message):
    chat_id = str(message.chat.id)

    if state.is_chat_exist(chat_id):
        bot.send_message(chat_id, f'Вы уже подписаны на уведомления')
    else:
        state.add(chat_id)
        bot.send_message(chat_id, f'Успешно подписались на уведомления! '
                                  f'\nУведомление о счете будет приходить каждый день в {SCHEDULE_TIME}, когда до '
                                  'окончания аренды сервера останется меньше *5-ти дней*.', parse_mode='Markdown')


@bot.message_handler(commands=['unsubscribe'])
def start(message):
    chat_id = str(message.chat.id)

    if state.is_chat_exist(chat_id):
        state.rm(chat_id)
        bot.send_message(chat_id, 'Успешно отписались от уведомлений!\nЧтобы подписаться, жмякни на /subscribe')
    else:
        bot.send_message(chat_id, 'Ты не подписан на уведомления')


@bot.message_handler(commands=['get_cloud_wallet'])
def start(message):
    chat_id = str(message.chat.id)
    bot.send_message(chat_id, reg_data_msg_action(), parse_mode='Markdown')
