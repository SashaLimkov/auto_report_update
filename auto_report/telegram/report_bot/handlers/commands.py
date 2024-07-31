from datetime import date
from aiogram import types
from aiogram.dispatcher import FSMContext
from TextData.services.text import get_language_by_name, get_default_language
from telegram.report_bot.utils.text import get_text
from aiogram.utils.deep_linking import decode_payload
from telegram.report_bot.data import text_data as td
from telegram.report_bot.utils.message_worker import try_edit_message
from telegram.report_bot.utils import deleter
from telegram.services import telegram_user as us
from telegram.report_bot.keyboards import inline as ik
from telegram.report_bot.keyboards import reply as rk
from telegram.report_bot.config.loader import bot
from telegram.report_bot.states.Modes import Mode
from telegram.report_bot.utils.fuzzy_search import find_nearest
from employers.services import telegram_employer as te
from aiogram.utils.markdown import hlink


async def main_menu(call: types.CallbackQuery, state: FSMContext):
    await start_command(message=call.message, state=state)



async def start_command(message: types.Message, state: FSMContext):
    args = message.get_args()
    data = await state.get_data()
    main_message_id = data.get("main_message_id", False)
    telegram_id = message.chat.id
    if args:
        text = await relate_employer_to_user(args=args, telegram_id=telegram_id, message=message)
    elif user:= us.get_user_by_id(telegram_id=telegram_id):
        lang = user.selected_language
        text = get_text(key=td.START_MESSAGE, lang=lang)
    else:
        text = get_text(key=td.NEED_QR, lang=get_default_language())
    user = us.get_user_by_id(telegram_id=telegram_id)
    name = hlink(user.redmine.first().user_name, user.redmine.first().redmine_url)
    print(name)
    text = text.format(name=name)
    await try_edit_message(
            telegram_id=telegram_id,
            text=text,
            main_message_id=main_message_id,
            state=state,
            keyboard=None,
        )
    await message.delete()


async def relate_employer_to_user(args:str, telegram_id:int, message:types.Message):
    redmine_id = decode_payload(args)
    print(redmine_id)
    employer = te.get_employer_by_id(redmine_id=redmine_id)
    user = us.get_user_by_id(telegram_id=telegram_id) or us.create_telegram_user(
        name=message.from_user.full_name, telegram_id=telegram_id
    )
    print(user)
    if not user.redmine.first():
        print(12324)
        employer.tg_user = user
        employer.save()
    return get_text(key=td.START_MESSAGE, lang=user.selected_language)
    
async def echo(message: types.Message, state: FSMContext):
    await message.reply(
        text=message.text
    )