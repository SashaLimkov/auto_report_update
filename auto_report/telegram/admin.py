from django.contrib import admin
from telegram.models import *

class MyAdminSite(admin.AdminSite):
    site_header = "Надстройки"
tg_admin = MyAdminSite(name="tg-admin")



tg_admin.register(TelegramUser)
tg_admin.register(Role)
