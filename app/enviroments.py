import os
from dotenv import load_dotenv

load_dotenv()

# Get environment variables
REG_RU_API_KEY = os.environ.get('REG_RU_API_KEY')
TG_BOT_API_KEY = os.environ.get('TG_BOT_API_KEY')
DATA_FILENAME = os.environ.get('DATA_FILENAME', default='data.txt')
SCHEDULE_TIME = os.environ.get('SCHEDULE_TIME', default='18:00')
REGION = os.environ.get('REGION', default='Europe/Moscow')
