
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

# bot = telebot.TeleBot('6531026375:AAHTVGDbN_FqCc3GAo4IrH3yFy6pre8M53w')
bot = Bot('6531026375:AAHTVGDbN_FqCc3GAo4IrH3yFy6pre8M53w')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app = WebAppInfo)
    await message.answer('Привет, мой друг!', reply_markup = markup)
# https: // www.youtube.com / watch?v = y65BZbNB0YA & list = PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt & index = 8

executor.start_polling(dp)