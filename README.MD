# reg-ru-notifications
Телеграм бот для уведомлений об облачном балансе в [reg.ru](https://www.reg.ru/)

## Команды бота
```
get_cloud_wallet - Текущий облачный счет
subscribe - Подписаться на уведомления
unsubscribe - Отписаться от уведомлений
pay_wallet - Пополнить облачный счет (опционально)
```

## Переменные окружения
```dotenv
# .env

REG_RU_API_KEY=your_reg_ru_api_key
TG_BOT_API_KEY=your_tg_bot_api_key


# Опциональные штуки

# Оплата
IS_PAYMENT = False | True
PAY_PROVIDER_TOKEN=your_pay_provider_token

REG_RU_URL='https://api.cloudvps.reg.ru/v1/balance_data'

# Название файла с списом чатов для рассылки уведомлений
DATA_FILENAME=data.txt

# Время для отправки уведомления 
SCHEDULE_TIME=18:00
REGION=Europe/Moscow

# Уведомление об окончании облачного счета за n дней
DAYS_LEFT_NOTIFICATION=5
```