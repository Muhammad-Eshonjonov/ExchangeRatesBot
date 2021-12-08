from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import keyboards as kb
from utils import Curs
from base import DBController

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

db = DBController("botbase.db")




@dp.callback_query_handler(lambda c: c.data == "usd")
async def process_callback_usd(callback_query: types.CallbackQuery):
    db.add_account(callback_query.from_user.id, "usd")
    await bot.send_message(callback_query.from_user.id, "Вы успешно добавлены\nВведите сумму")

@dp.callback_query_handler(lambda c: c.data == "uzb")
async def process_callback_usd(callback_query: types.CallbackQuery):
    db.add_account(callback_query.from_user.id, "uzb")
    await bot.send_message(callback_query.from_user.id, "Вы успешно добавлены\nВведите сумму")

@dp.callback_query_handler(lambda c: c.data == "rub")
async def process_callback_usd(callback_query: types.CallbackQuery):
    db.add_account(callback_query.from_user.id, "rub")
    await bot.send_message(callback_query.from_user.id, "Вы успешно добавлены\nВведите сумму")

@dp.callback_query_handler(lambda c: c.data == "tjk")
async def process_callback_usd(callback_query: types.CallbackQuery):
    db.add_account(callback_query.from_user.id, "tjk")
    await bot.send_message(callback_query.from_user.id, "Вы успешно добавлены\nВведите сумму")





@dp.message_handler(commands = ['start'])
async def process_start_command(msg: types.Message):
    if not db.get_user(msg.from_user.id):
        await bot.send_message(msg.from_user.id, f"Привет {msg.from_user.first_name} выберите свою валюту", reply_markup=kb.greet_kb1)
    else:
        await bot.send_message(msg.from_user.id, f"Рад снова видеть вас {msg.from_user.first_name} !!!\nУкажите сумму")


@dp.message_handler(commands = ['discharge'])
async def process_start_command(msg: types.Message):
    db.delete_user(msg.from_user.id)
    await bot.send_message(msg.from_user.id, "Вы успешно сброшены")


cs = Curs()

@dp.message_handler()
async def process_message_comand(msg: types.Message):
    if msg.text == 'Сомони 🇹🇯':
        try:
            saved = db.get_saved(msg.from_user.id)
            ans_bot = cs.ans(f"{saved}", "tjk")
            await bot.send_message(msg.from_user.id, f"{ans_bot}")
            await bot.send_message(msg.from_user.id, "Введите сумму")
        except:
            await bot.send_message(msg.from_user.id, "Вас нету в базу данных.\nВыберите свою валюту что бы добавить себя в базу данных", reply_markup=kb.greet_kb1)

    elif msg.text == 'Доллар 🇺🇸':
        try:
            saved = db.get_saved(msg.from_user.id)
            ans_bot = cs.ans(f"{saved}", "usd")
            await bot.send_message(msg.from_user.id, f"{ans_bot}")
            await bot.send_message(msg.from_user.id, "Введите сумму")
        except:
            await bot.send_message(msg.from_user.id, "Вас нету в базу данных.\nВыберите свою валюту что бы добавить себя в базу данных", reply_markup=kb.greet_kb1)

    elif msg.text == 'Рубль 🇷🇺':
        try:
            saved = db.get_saved(msg.from_user.id)
            ans_bot = cs.ans(f"{saved}", "rub")
            await bot.send_message(msg.from_user.id, f"{ans_bot}")
            await bot.send_message(msg.from_user.id, "Введите сумму")
        except:
            await bot.send_message(msg.from_user.id, "Вас нету в базу данных.\nВыберите свою валюту что бы добавить себя в базу данных", reply_markup=kb.greet_kb1)

    elif msg.text == 'Сум 🇺🇿':
        try:
            saved = db.get_saved(msg.from_user.id)
            ans_bot = cs.ans(f"{saved}", "uzb")
            await bot.send_message(msg.from_user.id, f"{ans_bot}")
            await bot.send_message(msg.from_user.id, "Введите сумму")
        except:
            await bot.send_message(msg.from_user.id, "Вас нету в базу данных.\nВыберите свою валюту что бы добавить себя в базу данных", reply_markup=kb.greet_kb1)
    else:
        try:
            x = int(msg.text)
            cs.valut(x)
            await bot.send_message(msg.from_user.id, "Выберите валюту которую хотите перевести эти суммы", reply_markup=kb.greet_kb)
        except:
            await bot.send_message(msg.from_user.id, "Пожалуйста введите сумму в цифрах !!!")

if __name__ == '__main__':
    executor.start_polling(dp)

