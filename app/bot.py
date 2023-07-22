import telebot
from telebot.types import LabeledPrice

from state import State
from enviroments import TG_BOT_API_KEY, SCHEDULE_TIME, DAYS_LEFT_NOTIFICATION, PAY_PROVIDER_TOKEN, IS_PAYMENT
from actions import reg_data_msg_action

state = State()
bot = telebot.TeleBot(TG_BOT_API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Oхайо, я умею уведомлять о текущем счете на сервере. жмякни на /subscribe '
                                      'чтобы подписаться на уведомления')


@bot.message_handler(commands=['subscribe'])
def start(message):
    if state.is_chat_exist(message.chat.id):
        bot.send_message(message.chat.id, f'Ты уже подписан на уведомления\nЧтобы отписаться, жмякни на /unsubscribe')
    else:
        state.add(message.chat.id)
        bot.send_message(message.chat.id, f'Успешно подписались на уведомления! '
                                          f'\nУведомление о счете будет приходить каждый день в *{SCHEDULE_TIME}*, когда до '
                                          f'окончания аренды сервера останется меньше *{DAYS_LEFT_NOTIFICATION} дн.*',
                         parse_mode='Markdown')


@bot.message_handler(commands=['unsubscribe'])
def start(message):
    if state.is_chat_exist(message.chat.id):
        state.rm(message.chat.id)
        bot.send_message(message.chat.id, 'Успешно отписались от уведомлений!\nЧтобы подписаться, жмякни на /subscribe')
    else:
        bot.send_message(message.chat.id, 'Ты не подписан на уведомления')


@bot.message_handler(commands=['get_cloud_wallet'])
def start(message):
    bot.send_message(message.chat.id, reg_data_msg_action(), parse_mode='Markdown')


@bot.message_handler(commands=['pay_wallet'])
def start(message):
    if IS_PAYMENT == 'True':
        bot.send_message(message.chat.id, 'Введи желаемую сумму для пополнения облачного счета', parse_mode='Markdown')
        bot.register_next_step_handler_by_chat_id(message.chat.id, create_payment)
    else:
        bot.send_message(message.chat.id, 'Оплата не подключена')


def create_payment(message):
    try:
        num_msg = int(message.text)
        price = num_msg * 100

        bot.send_invoice(
            chat_id=message.chat.id,
            title='Пополнение облачного счета',
            description=f'Пополнение облачного счета на {num_msg}₽',
            provider_token=PAY_PROVIDER_TOKEN,
            currency='rub',
            prices=[LabeledPrice('Пополнить облачное хранилище', price)],
            is_flexible=False,
            start_parameter='pay-cloud-wallet',
            invoice_payload='cloud-wallet')

    except ValueError:
        bot.send_message(message.chat.id, f'Необходимо ввести число. Повторите попытку')
    except Exception as e:
        print(f'Error: Something went wrong with create_payment\n{e}\n')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Произошла ошибка платежа. Повтори попытку позже")


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id,
                     f'Оплата на `{message.successful_payment.total_amount / 100}₽` '
                     'успешно произведена!\n'
                     'Облачный счет будет пополнен в течении некоторого времени!', parse_mode='Markdown')
