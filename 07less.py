from aiogram import Bot, Dispatcher, types, executor

# bot = telebot.TeleBot('6531026375:AAHTVGDbN_FqCc3GAo4IrH3yFy6pre8M53w')
bot = Bot('6531026375:AAHTVGDbN_FqCc3GAo4IrH3yFy6pre8M53w')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])#commands=['start'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer('Ты гений помни об этом ')
    await message.reply('Как сам чемпион ?')
    # await message.reply('/some.png', 'rb')

@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    murkup = types.InlineKeyboardMarkup()
    murkup.add(types.InlineKeyboardButton('Site', url = "https://www.google.com"))
    murkup.add(types.InlineKeyboardButton('Hello', callback_data ='Hello'))
    await message.reply('Hello', reply_markup=murkup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    murkup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    murkup.add(types.KeyboardButton('Site'))
    murkup.add(types.KeyboardButton('WebSite'))
    await message.answer('Hello', reply_markup=murkup)

executor.start_polling(dp)
