from aiogram import Dispatcher
from aiogram import filters
from . import commands
from TextData.services.text import get_default_language
from telegram.report_bot.utils.text import get_text
from telegram.report_bot.data import text_data as td
from telegram.report_bot.states.Modes import Mode


def setup(dp: Dispatcher):
    dp.register_message_handler(
        commands.start_command, filters.CommandStart(), state="*"
    )
    dp.register_message_handler(
        commands.echo, state="*"
    )
    # dp.register_callback_query_handler(
    #     commands.main_menu, filters.Text(td.BACK_MM_KB), state="*"
    # )
    # dp.register_callback_query_handler(
    #     commands.switch_language, filters.Text(endswith="_lang"), state="*"
    # )
    # dp.register_callback_query_handler(
    #     main_module.get_original, filters.Text(td.START_RATE_KB), state="*"
    # )
    # dp.register_callback_query_handler(
    #     main_module.save_user_answer, filters.Text(startswith="answer_"), state="*"
    # )
    # dp.register_callback_query_handler(
    #     main_module.skip_user_answer, filters.Text(td.NEXT_RATE_KB), state="*"
    # )
    # dp.register_callback_query_handler(
    #     stat.show_stat, filters.Text(td.STAT_KB), state="*"
    # )
    # registration_module.setup(dp)
    # main_module.setup(dp)
    # dp.register_message_handler(commands.start_command, filters.CommandStart(), state="*")
    # dp.register_message_handler(commands.stat, filters.Text("Статистика"), state="*")
    # dp.register_callback_query_handler(commands.main_menu, filters.Text("mm"), state="*")
