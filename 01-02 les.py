import telebot
import webbrowser

bot = telebot.TeleBot('6531026375:AAF7WoOEEogVcI-UtKhe9Y3ptYC3gZNW6nY')


@bot.message_handler(command=['site', 'website'])
def site(message):
    webbrowser.open('https://coinmarketcap.com/')
@bot.message_handler(commands=['start', 'hello', 'world'])
def main(message):
    bot.send_message(message.chat.id, 'ТЫ ГЕНИЙ!!!')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
# bot.infinity_polling()
