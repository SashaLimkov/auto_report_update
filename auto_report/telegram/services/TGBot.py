from telegram.models import TGBot


def get_bot_token(bot_name: str):
    return get_bot(bot_name=bot_name).token


def get_bot(bot_name: str):
    return TGBot.objects.filter(name=bot_name).first()
