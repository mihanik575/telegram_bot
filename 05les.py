#https://www.youtube.com/watch?v=v8Nqa78v2tE&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=5
#https://home.openweathermap.org/api_keys
import telebot

bot = telebot.TeleBot('6531026375:AAF7WoOEEogVcI-UtKhe9Y3ptYC3gZNW6nY')
API = '51a672a644f481794d9e44dab6e1c00c'

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города:')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()


bot.polling(none_stop=True)