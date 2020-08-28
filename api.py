# telegram api with python
# playing with telegram bot api in testing different methods

import requests
import os
import random
bot_token = os.environ.get("BOT_TOKEN")
url = f"https://api.telegram.org/bot{bot_token}/"
stripe_test_token = os.environ.get("STRIPE_TEST_TOKEN")

def get_chat_id(update):
    chat_id=update['message']['chat']['id']
    return chat_id

def get_name(update):
    first_name =update['message']['chat']['first_name']
    last_name =update['message']['chat']['last_name']
    return f'{first_name} {last_name}'

def get_message_text(update):
    message_text = update['message']['text']
    return message_text

def last_update(req):
    response = requests.get(req + 'getUpdates')
    response = response.json()
    result = response['result']
    total_updates = len(result)-1
    return result[total_updates]
    
    
def send_message(chat_id, text):
    params={
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url + 'sendMessage', data = params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            name=get_name(update)
            if get_message_text(update).lower() == '/hi' or get_message_text(update).lower()=='/hello':
                send_message(get_chat_id(update), f"Hello {name}, welcome to Salom Pay bot. /hello, /hi or /play")
            elif get_message_text(update).lower() == '/play':
                send_message(get_chat_id(update), "ohhh you wanna play then? huh? okay...")
            else:
                send_message(get_chat_id(update), f"Didnt get what you mean, {name},  please choose between /hello, /hi or /play",)
            update_id += 1




main()











