from telegram.models import TelegramUser

def create_telegram_user(name:str, telegram_id:int, username:str = None):
    # user = TelegramUser(
    #     name=name,
    #     telegram_id=telegram_id,
    #     username=username
    # )
    # user.save()
    # return user
    return TelegramUser.objects.create(
        name=name,
        telegram_id=telegram_id,
        username=username
    )


def get_all_users():
    return TelegramUser.objects.all()

def get_user_by_id(telegram_id: int):
    return TelegramUser.objects.filter(telegram_id=telegram_id).first()

def update_name(telegram_id:int, name:str):
    user = get_user_by_id(telegram_id=telegram_id)
    user.name = name
    user.save()
    
def delete_all_users():
    TelegramUser.objects.all().delete()
    