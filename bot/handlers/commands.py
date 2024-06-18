from aiogram import Dispatcher
from aiogram.filters import Command

from bot.handlers.start import start_command
from bot.handlers.main_menu import my_subs, add_sub_command, delete_sub_command, delete_sub_process, add_sub_process
from bot.utils.TextFilter import TextFilter

from bot.texts.buttons import *
from bot.states import Form


def register_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command(commands=["start"]))

    dp.message.register(my_subs, TextFilter(MY_SUBS))
    dp.message.register(add_sub_command, TextFilter(ADD_SUB))
    dp.message.register(delete_sub_command, TextFilter(DELETE_SUB))

    dp.message.register(delete_sub_process, Form.delete_sub)
    dp.message.register(add_sub_process, Form.add_sub)

