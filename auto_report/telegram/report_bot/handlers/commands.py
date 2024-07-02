from datetime import date
from aiogram import types
from aiogram.dispatcher import FSMContext
from TextData.services.text import get_language_by_name, get_default_language
from telegram.report_bot.utils.text import get_text

from telegram.report_bot.data import text_data as td
from telegram.report_bot.utils.message_worker import try_edit_message
from telegram.report_bot.utils import deleter
from telegram.services import telegram_user as us
from telegram.report_bot.keyboards import inline as ik
from telegram.report_bot.keyboards import reply as rk
from telegram.report_bot.config.loader import bot
from telegram.report_bot.states.Modes import Mode
from telegram.report_bot.utils.fuzzy_search import find_nearest


async def main_menu(call: types.CallbackQuery, state: FSMContext):
    await start_command(message=call.message, state=state)


async def start_command(message: types.Message, state: FSMContext):
    data = await state.get_data()
    main_message_id = data.get("main_message_id", False)
    telegram_id = message.chat.id
    user = us.get_user_by_id(telegram_id=telegram_id) or us.create_telegram_user(
        name=message.from_user.full_name, telegram_id=telegram_id
    )
    lang = user.selected_language
    text = get_text(key=td.START_MESSAGE, lang=lang)
    await try_edit_message(
        telegram_id=telegram_id,
        text=text,
        main_message_id=main_message_id,
        state=state,
        keyboard=None,
    )
    await message.delete()


async def echo(message: types.Message, state: FSMContext):
    await message.reply(
        text=message.text
    )