from backend.models import TimeBasedModel
from TextData.models import Language
from django.db import models


class TelegramUser(TimeBasedModel):
    class Meta:
        verbose_name = "Телеграм Юзер"
        verbose_name_plural = "Телеграм Юзеры"
        ordering = ["-name"]
        
    name = models.CharField("ФИО из ТГ", max_length=128)
    telegram_id = models.BigIntegerField("Телеграм ID", unique=True)
    username = models.CharField("Ник Телеграм", max_length=128, null=True, blank=True, default=None)
    selected_language = models.ForeignKey(
        Language,
        verbose_name="Выбранный язык",
        on_delete=models.DO_NOTHING,
        related_name="users",
        null=True,
        blank=True,
        default=None,
    )
    role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name="users", verbose_name="Роль пользователя")
    bot = models.ForeignKey(
        "TGBot",
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="users",
    )

    
    
    def __str__(self):
        return f"{self.name} {self.telegram_id} {self.pk}"
    

class Role(TimeBasedModel):
    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
        ordering = ["-name"]
        
    name = models.CharField(verbose_name="Название роли", max_length=255) 
    
    def __str__(self) -> str:
        return self.name
    
    
class TGBot(TimeBasedModel):
    class Meta:
        verbose_name = "Бот"
        verbose_name_plural = "Боты"
        ordering = ["name"]

    name = models.CharField("Название бота", max_length=255)
    token = models.CharField("Токен бота", max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
