import os
import sqlite3
import telebot

bot = telebot.TeleBot('6531026375:AAF7WoOEEogVcI-UtKhe9Y3ptYC3gZNW6nY')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('bazasdelok.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50)), pass varchar(50)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введи своё имя?' )
    bot.register_next_step_handler(message, user_name)

def user_name(message):
#https://www.youtube.com/watch?v=f2z4uuDJO3c&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=4

bot.polling(none_stop=True)