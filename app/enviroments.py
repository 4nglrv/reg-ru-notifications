import os
from dotenv import load_dotenv

load_dotenv()

# Get environment variables
REG_RU_API_KEY = os.environ.get('REG_RU_API_KEY')
TG_BOT_API_KEY = os.environ.get('TG_BOT_API_KEY')

IS_PAYMENT = os.environ.get('IS_PAYMENT', default=False)
PAY_PROVIDER_TOKEN = os.environ.get('PAY_PROVIDER_TOKEN')

REG_RU_URL = os.environ.get('REG_RU_URL', default='https://api.cloudvps.reg.ru/v1/balance_data')

DATA_FILENAME = os.environ.get('DATA_FILENAME', default='data.txt')

SCHEDULE_TIME = os.environ.get('SCHEDULE_TIME', default='18:00')
REGION = os.environ.get('REGION', default='Europe/Moscow')
DAYS_LEFT_NOTIFICATION = os.environ.get('DAYS_LEFT_NOTIFICATION', default=30)