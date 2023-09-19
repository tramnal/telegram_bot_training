import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6277525733:AAFJFbr4CpmCDNvYrm2sMamNjnAOI_gkDqg'
TEXT = 'Салам Алейкум!'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int
