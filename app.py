import os
from flask import Flask, request
import telebot
import json
import requests
from config import TOKEN, HEROKU_URL, TWITCH_API, TW_CH, JSON_TWITCH_REQ, TOPIC, TWITCH_URL, CHAT_ID, TWITCH_CLIENT_ID, APP_ACCESS_TOKEN

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url= HEROKU_URL + TOKEN)
    twitch_sub_webhook()    # Maximum duration 10days
    return "!", 200


@server.route("/" + TW_CH, methods=['GET', 'POST'])
def live():
    if request.method == 'GET':
        token = request.args.get('hub.challenge')
        if token is not None:
            return str(token)
        return 'Some problems!'  # Some problems with Ack Webhook
    else:
        response = request.get_json()
        status = response['data'][0]
        if status is not None:
            title = status['title']
            bot.send_message(CHAT_ID, 'Hey, sono live! Vieni a vedermi: {}\nTitolo: {}'.format(TWITCH_URL, title))
        return 'Ok POST! {}'.format(title)
    return "Error!"

def twitch_sub_webhook():
    headers = {
        'Content-type': 'application/json',
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': 'Bearer ' + APP_ACCESS_TOKEN
        }
    requests.post(TWITCH_API, json.dumps(JSON_TWITCH_REQ), headers=headers)


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))