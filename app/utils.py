def strip_file_lines(arr: list):
    newArr = []
    for line in arr:
        newArr.append(str(line).strip())

    return newArr


def wallet_msg(data: object):
    balance = data["balance_data"]["balance"]
    days_left = data["balance_data"]["days_left"]
    monthly_cost = data["balance_data"]["monthly_cost"]

    message = f'Облачный счет составляет *{balance} ₽*\n' \
              f'Этого хватит на *{days_left} дн.*\n' \
              f'Расход средств и прогноз потребления: *{monthly_cost} ₽/месяц*'

    return message
