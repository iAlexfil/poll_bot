from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.texts.buttons import *

main_menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MY_SUBS)],
    [KeyboardButton(text=DELETE_SUB),
     KeyboardButton(text=ADD_SUB)]
], resize_keyboard=True)

admin_menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MAKE_SENDING)],
    [KeyboardButton(text=MAKE_EVENT)],
    [KeyboardButton(text=EXIT_ADMIN)]
], resize_keyboard=True)

