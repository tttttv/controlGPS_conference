# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : fabston               #
# File Name             : main.py               #
# --------------------------------------------- #

import config
from resources import mysql_handler as mysql
from resources import markups_handler as markup
from resources import msg_handler as msg

import telebot
from datetime import datetime
import arrow

bot = telebot.TeleBot(config.token)

mysql.createTables

# Start Command
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        print('USERNAME!!!')
        username = message.from_user.username
        if username == None:
            username = 'NoTag'
        # else:
        #    username = username.replace("_"," ")
        from_user_id = message.from_user.id if message.from_user.id else ''
        st = f'Got message from {from_user_id}, type: {message.content_type}'
        if message.content_type == 'text':
            msg = bot.send_message(config.support_chat, "[{0}{1}], tg:@{4} (#id{2})\n\n{3}".format(
                message.from_user.first_name,
                ' {0}'.format(message.from_user.last_name) if message.from_user.last_name else '',
                from_user_id, message.text, username), parse_mode='HTML', disable_web_page_preview=True)

        bot.send_message(message.chat.id,
                         config.text_messages['start'],
                         parse_mode='Markdown', disable_web_page_preview=True)
        mysql.start_bot(message.chat.id)
    else:
        bot.reply_to(message, 'Если вы хотите получить ответ от техподдержки, напишите мне в личные сообщения.')

print("Telegram Support Bot started...")
bot.polling()
