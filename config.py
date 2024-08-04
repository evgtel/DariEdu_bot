# t.me/QAP166_bot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
#TOKEN = '7025670714:AAGHAXF9fIj8lAMvmY7qhxbhzvsxABIcXPM'
currency = {'рубль': 'RUB',
            'доллар': 'USD',
            'евро': 'EUR'}
