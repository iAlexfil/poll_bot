from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.db import exist_user, add_user
from bot.utils.keyboards import main_menu_kb


async def start_command(message: types.Message, state: FSMContext):
    if not exist_user(message.from_user.id):
        add_user(message.from_user.id, message.from_user.username)

    await message.answer("Добро пожаловать в бота!", reply_markup=main_menu_kb)
    await state.clear()



