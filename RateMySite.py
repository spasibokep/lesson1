# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Отчеты о работе бота
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# когда пользователь пишет /start вручную или подключится к боту в первый раз   
def greet_user(bot, update):
    text = "Привет, я искусственный интеллект, который оценивает сайты. Дай мне ссылку - и я сделаю линч"
    print(text)
    update.message.reply_text(text)

# Функция, которая отвечает пользователю
def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    updater = Updater("478219449:AAGsEUulnylbTRnKlbFDP8VqosdfGneCako")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()
