from aiogram import types
from aiogram.fsm.context import FSMContext
from bot.states import AdminForm
from bot.db import make_event
from bot.utils.keyboards import admin_menu_kb


name = ''


async def make_event_command(message: types.Message, state: FSMContext):
    await message.answer('Введите название нового ивента', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AdminForm.make_event)


async def process_name(message: types.Message, state: FSMContext):
    global name
    if not name:
        name = message.text
        await message.answer('Введите описание ивента')
    else:
        description = message.text
        event_id = make_event(name, description)
        name = ''
        await message.answer(f'рассылка создана с id = {event_id}', reply_markup=admin_menu_kb)
        await state.set_state(AdminForm.menu)
