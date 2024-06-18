from aiogram import types
from aiogram.fsm.context import FSMContext
from bot.states import AdminForm
from bot.db import make_event, get_all_users, exist_sub
from bot.utils.keyboards import admin_menu_kb


event_id = -1


async def make_sending_command(message: types.Message, state: FSMContext):
    await message.answer('Введите id события, по которому создать рассылку', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AdminForm.make_sending)


async def process_sending(message: types.Message, state: FSMContext):
    global event_id
    if event_id == -1:
        event_id = int(message.text)
        await message.answer('Введите сообщение для рассылки')
    else:
        count = 0
        for user in get_all_users():
            if not exist_sub(user, event_id):
                continue
            try:
                await message.bot.copy_message(chat_id=user,
                                               from_chat_id=message.from_user.id,
                                               message_id=message.message_id)
                count += 1
            except Exception as e:
                pass
        await message.answer(f'Рассылка успешно завершена, доставлено сообщений: {count}', reply_markup=admin_menu_kb)
        await state.set_state(AdminForm.menu)