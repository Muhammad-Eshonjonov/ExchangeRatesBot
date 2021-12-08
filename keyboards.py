from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_tjk = KeyboardButton('Сомони 🇹🇯')
btn_usd = KeyboardButton('Доллар 🇺🇸')
btn_rub = KeyboardButton('Рубль 🇷🇺')
btn_uzb = KeyboardButton('Сум 🇺🇿')

inline_btn_tjk = InlineKeyboardButton('Сомони 🇹🇯', callback_data='tjk')
inline_btn_usd = InlineKeyboardButton('Доллар 🇺🇸', callback_data='usd')
inline_btn_rub = InlineKeyboardButton('Рубль 🇷🇺', callback_data='rub')
inline_btn_uzb = InlineKeyboardButton('Сум 🇺🇿', callback_data='uzb')

greet_kb1 = InlineKeyboardMarkup().row(
    inline_btn_rub, inline_btn_usd
).row(
    inline_btn_uzb, inline_btn_tjk
)

greet_kb = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)

greet_kb.row(btn_tjk, btn_usd).row(btn_uzb, btn_rub)