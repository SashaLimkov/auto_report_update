from backend.models import TimeBasedModel
from django.db import models


class TelegramUser(TimeBasedModel):
    class Meta:
        verbose_name = "Телеграм Юзер"
        verbose_name_plural = "Телеграм Юзеры"
        ordering = ["-name"]
        
    name = models.CharField("ФИО из ТГ", max_length=128)
    telegram_id = models.BigIntegerField("Телеграм ID", unique=True)
    username = models.CharField("Ник Телеграм", max_length=128, null=True, blank=True, default=None)
    role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name="users", verbose_name="Роль пользователя")
    
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
    