import telebot
from bot_token import TOKEN
import config
from flask import Flask, request
import logging
import os



bot = telebot.TeleBot(TOKEN)



@bot.message_handler(content_types=['new_chat_members'])
def chek(message):
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
def kill_phrases(message):
    bot.send_message(message.chat.id, 'Cheking')
    for word in config.bad_words:
        if word in message.text:
            bot.send_message(message.chat.id, 'Gay')
            bot.delete_message(message.chat.id, message.message_id)
            bot.kick_chat_member(message.chat.id, message.from_user.id)


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
server = Flask(__name__)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='your heroku project.com' + TOKEN)
    return "?", 200


server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))