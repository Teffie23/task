import config
import logging
from aiogram import types,Bot,Dispatcher,executor
import sqlite3
logging.basicConfig(level=logging.INFO)
bot=Bot(token=config.TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('Получить ID пользывателя из Inline кнопки', callback_data='user_id')
    keyboard_markup.row(user_id_btn)
    await message.answer(f"Ваш ID: {message.from_user.id}", reply_markup=keyboard_markup)
@dp.callback_query_handler(lambda c: c.data == 'user_id')
async def user_id_inline_callback(callback_query: types.CallbackQuery):
    await callback_query.answer(f"Ваш ID: {callback_query.from_user.id}", True)
@dp.message_handler()
async def echo(message: types.Message):
    with sqlite3.connect('wallet1.db') as db:
        cursor= db.cursor()
        s= message.text
        cursor.execute("SELECT users.Name, users.balance FROM users WHERE name=?",[s])
        for x in cursor.fetchall():
            await message.answer(x)
            await bot.send_message(message.from_user.id,x)
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)