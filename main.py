import telebot
from bot_token import TOKEN
import config


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['new_chat_members'])
def chek(message):
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
def kill_phrases(message):
    for word in config.bad_words:
        if word in message.text:
            bot.delete_message(message.chat.id, message.message_id)
            bot.kick_chat_member(message.chat.id, message.from_user.id)



if __name__ == '__main__':
    bot.polling(none_stop=True)