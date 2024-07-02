from aiogram.dispatcher.filters.state import StatesGroup, State


class Mode(StatesGroup):
    INV = State()
    NAME = State()
    SERIAL = State()
