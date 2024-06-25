from django.contrib import admin
from telegram.admin import tg_admin
from TextData.models import Text, Language, Translate


# Register your models here.
class TranslatesAdmin(admin.ModelAdmin):
    list_display = ("text_key", "language", "translate")
    list_display_links = ("translate",)
    raw_id_fields = ("text_key", "language")
    search_fields = ("Translate",)
    list_filter = ("language",)


class TranslatesInline(admin.StackedInline):
    model = Translate
    fields = ["text_key", "language", "translate"]
    show_change_link = True
    extra = 0


class TextAdmin(admin.ModelAdmin):
    list_display = ("key", "key_type")
    inlines = [TranslatesInline]
    list_filter = ("key_type",)


tg_admin.register(Language)
tg_admin.register(Translate, TranslatesAdmin)
tg_admin.register(Text, TextAdmin)
