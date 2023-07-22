import requests
import json

from enviroments import REG_RU_API_KEY, REG_RU_URL, DAYS_LEFT_NOTIFICATION, IS_PAYMENT
from utils import wallet_msg


def request_to_reg_action():
    try:
        response = requests.get(REG_RU_URL, headers={
            "Authorization": REG_RU_API_KEY
        })
        data = json.loads(response.content)
        print(f'Response: {data}')

        return data
    except Exception as e:
        print(f'Error: Something went wrong in request_to_reg_action.\n{e}\n')


def reg_notification_msg_action(state, bot):
    data = request_to_reg_action()

    try:
        days_left = data["balance_data"]["days_left"]
        message = f'*Пора пополнить облачный счет!*\n\n' \
                  f'{wallet_msg(data)}\n'

        pay_message = 'Для пополнения облачного счета, нажми на /pay_wallet'

        if len(state.chats) and days_left <= int(DAYS_LEFT_NOTIFICATION):
            for chat in state.chats:
                bot.send_message(chat, message, parse_mode='Markdown')

                if IS_PAYMENT == 'True':
                    bot.send_message(chat, pay_message)
            print(f'Notifications is sended for all chat_id')

    except Exception as e:
        print(f'Error: Something went wrong with notifications.\n{e}\n')


def reg_data_msg_action():
    data = request_to_reg_action()
    return wallet_msg(data)
