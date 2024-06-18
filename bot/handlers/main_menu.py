from aiogram import types
from aiogram.fsm.context import FSMContext
from bot.db import get_subs, delete_sub, add_sub
from bot.utils.keyboards import main_menu_kb

from bot.states import Form


async def my_subs(message: types.Message, state: FSMContext):
    await message.answer("Вот рассылки на которые вы подписаны")
    subs = get_subs(message.from_user.id)
    ans = f'Всего подписок : {len(subs)}\n'
    for event_id, name in subs:
        ans += f'\nid: {event_id}\nназвание: {name}\n'
    await message.answer(ans)


async def delete_sub_command(message: types.Message, state: FSMContext):
    await message.answer('''Пожалуйста, введите id рассылки, от которой хотите отписаться''',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Form.delete_sub)


async def add_sub_command(message: types.Message, state: FSMContext):
    await message.answer('''Пожалуйста, введите id рассылки, на которую хотите подписаться''',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Form.add_sub)


async def delete_sub_process(message: types.Message, state: FSMContext):
    try:
        event_id = int(message.text)
    except ValueError:
        await message.answer('Вы ввели некорректный id', reply_markup=main_menu_kb)
        await state.clear()
        return

    if delete_sub(message.from_user.id, event_id):
        await message.answer('Вы успешно отписались от рассылки', reply_markup=main_menu_kb)
    else:
        await message.answer('Вы не подписаны на рассылку с таким id', reply_markup=main_menu_kb)

    await state.clear()


async def add_sub_process(message: types.Message, state: FSMContext):
    try:
        event_id = int(message.text)
    except ValueError:
        await message.answer('Вы ввели некорректный id', reply_markup=main_menu_kb)
        await state.clear()
        return

    if add_sub(message.from_user.id, event_id):
        await message.answer(f'Вы успешно подписались на рассылку {event_id}', reply_markup=main_menu_kb)
    else:
        await message.answer(f'Рассылки с таким id не существует', reply_markup=main_menu_kb)

    await state.clear()
