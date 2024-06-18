from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    delete_sub = State()
    add_sub = State()


class AdminForm(StatesGroup):
    menu = State()
    make_sending = State()
    make_event = State()
