from telegram.report_bot.utils.base_keyboard_utils import (
    get_base_keyboard,
    get_keyboard_button,
)
from telegram.report_bot.data import text_data as td
from telegram.report_bot.utils.text import get_text
from TextData.services.text import get_default_language

# __all__ = [
#     "modes",
# ]


# async def modes():
#     lang = get_default_language()
#     keyboard = await get_base_keyboard(
#         keyboard_options={
#             "row_width": 1,
#             "resize_keyboard": True,
#         },
#         is_inline=False,
#         buttons=[
#             {"text": get_text(key=td.INV_KB, lang=lang)},
#             {"text": get_text(key=td.BY_NAME_KB, lang=lang)},
#             {"text": get_text(key=td.SERIAL_KB, lang=lang)},
#         ],
#     )
#     return keyboard
