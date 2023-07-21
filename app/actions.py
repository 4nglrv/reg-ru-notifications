import requests
import json

from enviroments import REG_RU_API_KEY, DAYS_LEFT_NOTIFICATION
from utils import wallet_msg


def request_to_reg_action():
    response = requests.get('https://api.cloudvps.reg.ru/v1/balance_data', headers={
        "Authorization": REG_RU_API_KEY
    })
    data = json.loads(response.content)
    print(f'Response: {data}')

    return data


def reg_notification_msg_action(state, bot):
    data = request_to_reg_action()
    days_left = data["balance_data"]["days_left"]
    message = f'*Пора пополнить облачный счет*\n{wallet_msg(data)}'

    if len(state.chats) and days_left <= DAYS_LEFT_NOTIFICATION:
        for chat in state.chats:
            bot.send_message(chat, message, parse_mode='Markdown')


def reg_data_msg_action():
    data = request_to_reg_action()
    return wallet_msg(data)
