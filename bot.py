import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Пашок (｡◕‿◕｡)')


bot.polling(none_stop=True)
