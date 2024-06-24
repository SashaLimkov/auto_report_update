from django.db import models
from backend.models import TimeBasedModel
from telegram.models import TelegramUser


class Employer(TimeBasedModel):
    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчики"
        ordering = ["-user_name"]
        
    # мейби стоит назвать developer или employer_name
    user_name: str = models.CharField("ФИО разработчика", max_length=128)
    tg_urls: str = models.ForeignKey(TelegramUser, on_delete=models.SET_NULL,null=True, verbose_name="Ссылка на телеграм")
    start_time: str = models.DateTimeField("Начало рабочего дня")
    end_time: str = models.DateTimeField("Конец рабочего дня")
    employer_status: str = models.FloatField("Текущая занятость")

    def __str__(self):
        return self.user_name

