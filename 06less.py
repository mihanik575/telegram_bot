import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6531026375:AAF7WoOEEogVcI-UtKhe9Y3ptYC3gZNW6nY')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет введите сумму?')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Впишите корректное число')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 10:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Другое', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Минимальная сумма сделки 10. Впишите сумму больше')
        bot.register_next_step_handler(message, summa)
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    values = call.data.upper().split('/')
    res = currency.convert(amount, values[0], values[1])
    bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}. Можете заново ввести число')
    bot.register_next_step_handler(call.message, summa)
    # print(amount)
    # print(values[0])
    # print(values[1])
    print(res)

# https://www.youtube.com/watch?v=YrDL6EpYNiA&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=6
# print(currency.convert(50, 'USD', 'EUR'))
bot.polling(none_stop=True)