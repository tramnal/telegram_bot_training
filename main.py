import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6277525733:AAFJFbr4CpmCDNvYrm2sMamNjnAOI_gkDqg'
TEXT = 'Салам Алейкум!'
MAX_COUNTER = 10

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    print(updates)

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1
