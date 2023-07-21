import os
from dotenv import load_dotenv

load_dotenv()

# Get environment variables
REG_RU_API_KEY = os.getenv('REG_RU_API_KEY')
TG_BOT_API_KEY = os.getenv('TG_BOT_API_KEY')
DATA_FILENAME = os.getenv('DATA_FILENAME', default='data.txt')
SCHEDULE_TIME = os.getenv('SCHEDULE_TIME', default='18:00')
REGION = os.getenv('REGION', default='Europe/Moscow')
