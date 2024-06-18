from aiogram import Dispatcher
from aiogram.filters import Command
from bot.utils.TextFilter import TextFilter, LowerTextFilter
from bot.utils.keyboards import admin_menu_kb, main_menu_kb
from bot.texts.buttons import *

from bot.db import is_admin

from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.admin.make_event import make_event_command, process_name
from bot.admin.make_sending import make_sending_command, process_sending

from bot.states import AdminForm


async def enter_admin_mode(message: types.Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        return
    await message.answer('Добро пожаловать в меню админа!', reply_markup=admin_menu_kb)
    await state.set_state(AdminForm.menu)


async def exit_admin_mode(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в главное меню!', reply_markup=main_menu_kb)
    await state.clear()


def register_handlers(dp: Dispatcher):
    dp.message.register(enter_admin_mode, LowerTextFilter('админ'))
    dp.message.register(exit_admin_mode, TextFilter(EXIT_ADMIN))
    dp.message.register(make_event_command, AdminForm.menu, TextFilter(MAKE_EVENT))
    dp.message.register(process_name, AdminForm.make_event)

    dp.message.register(make_sending_command, AdminForm.menu, TextFilter(MAKE_SENDING))
    dp.message.register(process_sending, AdminForm.make_sending)

