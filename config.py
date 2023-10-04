# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : fabston               #
# File Name             : config.py             #
# --------------------------------------------- #

# Telegram
token = '6562629843:AAEg69AYiWO43MznA675PgZ2StYCsTZq-rE'      # More: https://core.telegram.org/bots#3-how-do-i-create-a-bot

# MySQL Database
mysql_host = 'localhost'
mysql_db   = 'TelegramSupportBot'
mysql_user = 'SupportBotUser'
mysql_pw   = 'password'

# Support Chat (Chat ID)
support_chat = -4034650871  # Example: -1001429781350 | To find out your channels ID use: https://t.me/getidsbot

# Misc
time_zone           = 'GMT+3'   # Supports time zone
bad_words_toggle    = False      # Enable / disable bad words filter
spam_toggle         = False      # Enable / disable spam filter
spam_protection     = 5         # How many consecutive messages can be sent without a reply from the team
open_ticket_emoji   = 24        # After X amount of HOURS an emoji will pop up at /tickets

# Messages
text_messages = {
    'start': 'Добрый день. Пожалуйста, укажите название вашего парка и напишите вопрос в чат, наши специалисты ответят на него в ближайшее время.',
    'faqs': 'Напишите ваш вопрос в чат, и наши специалисты ответят на него',
    'support_response': 'С увважением, {}, ControlGPS'                  # Support response is being added automatically. {} = refers to the staffs first name.
}

# Regex (https://regex101.com/)
regex_filter = {
    'bad_words': r'(?i)^(.*?(\b\w*fuck|shut up|dick|bitch|bastart|cunt|bollocks|bugger|rubbish|wanker|twat|suck|ass|pussy|arsch\w*\b)[^$]*)$'
}
