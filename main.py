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
                         """[ControlGPS](http://controlgps.org/) - cовременная  система GPS мониторинга таксопарка от 150₽ в месяц за авто.
\n
🛰️ Подключаем ваше текущее или устанавливаем наше надежное оборудование за 3499₽
\n
﻿﻿🚖Прямая интеграция с Яндекс Такси для автоматического глушения по отрицательному балансу водителя. 
\n
﻿﻿🚨 Глушение авто в одно нажатие через сайт или мобильное приложение Android и IOS.
\n
﻿﻿🗺️ Контроль выезда из города или указанной геозоны.
\n
﻿﻿👨‍💻 Круглосуточная поддержка клиентов 24/7
\n
Интересно стать нашим партнером в своем регионе? Вся информация на [controlgps.org/franchise](http://controlgps.org/franchise)
\n
[Нажмите чтобы оставить заявку на подключение системы](http://controlgps.org/)""",
                         parse_mode='Markdown', disable_web_page_preview=True)
        mysql.start_bot(message.chat.id)
    else:
        bot.reply_to(message, 'Если вы хотите получить ответ от техподдержки, напишите мне в личные сообщения.')

# Message Forward Handler (User - Support)
@bot.message_handler(func=lambda message: message.chat.type == 'private', content_types=['text', 'photo', 'document', 'video', 'voice'])
def echo_all(message):
    while True:
        mysql.start_bot(message.chat.id)
        user_id = message.chat.id
        message = message

        try:
            ticket_status = mysql.user_tables(user_id)['open_ticket']
            ticket_spam = mysql.user_tables(user_id)['open_ticket_spam']

            if ticket_status == 0:
                mysql.open_ticket(user_id)
                continue
            else:
                msg.fwd_handler(user_id, bot, message)
                return
        except:
            bot.reply_to(message, 'Сообщение не доставлено')

print("Telegram Support Bot started...")
bot.polling()
