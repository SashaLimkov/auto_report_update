from telegram.report_bot.utils.base_keyboard_utils import (
    get_base_keyboard,
    get_inline_button,
)
from telegram.report_bot.data import text_data as td
from telegram.report_bot.utils.text import get_text
from TextData.services.text import get_default_language
from TextData.models import Language



__all__ = ["back",]

async def main_keyboard(lang:Language = get_default_language()):
    keyboard = await get_base_keyboard(
        keyboard_options={
            "row_width": 1,
        },
    )
    



async def back():
    lang = get_default_language()
    keyboard = await get_base_keyboard(
        keyboard_options={
            "row_width": 2,
        },
    )
    keyboard.add(
        await get_inline_button(
            text=get_text(key=td.BACK_MM_KB, lang=lang), cd=td.BACK_MM_KB
        )
    )
    return keyboard
