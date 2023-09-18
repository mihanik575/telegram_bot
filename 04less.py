import sqlite3
import telebot

bot = telebot.TeleBot('6531026375:AAF7WoOEEogVcI-UtKhe9Y3ptYC3gZNW6nY')
name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('bazasdelok.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введи своё имя?' )
    bot.register_next_step_handler(message, user_name)

def user_name(message): # обработка сообщения пользователя
    global name
    name = message.text.strip() #удаляет пробелы до и после функции
    bot.send_message(message.chat.id, 'Введите пароль:' )
    bot.register_next_step_handler(message, user_pass)

def user_pass(message): # обработка сообщения пользователя
    password = message.text.strip() #удаляет пробелы до и после функции

    conn = sqlite3.connect('bazasdelok.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    murkup = telebot.types.InlineKeyboardMarkup()
    murkup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=murkup)
    # bot.send_message(message.chat.id, 'Введите пароль:' )
    # bot.register_next_step_handler(message, user_pass)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('bazasdelok.sql')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)