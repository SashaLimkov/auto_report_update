from django.db import models
from backend.models import TimeBasedModel
from telegram.models import TelegramUser
from django.utils.safestring import mark_safe


class Employer(TimeBasedModel):
    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчики"
        ordering = ["-user_name"]
        
    # мейби стоит назвать developer или employer_name
    user_name: str = models.CharField("ФИО разработчика", max_length=128)
    redmine_id = models.CharField("ID redmine", max_length=3, null=True, blank=True)
    redmine_url = models.CharField("URL redmine", max_length=128, null=True, blank=True)
    tg_user: str = models.ForeignKey(TelegramUser, on_delete=models.SET_NULL, null=True, verbose_name="Ссылка на телеграм", related_name="redmine")
    start_time: str = models.DateTimeField("Начало рабочего дня", null=True, blank=True)
    end_time: str = models.DateTimeField("Конец рабочего дня", null=True, blank=True)
    employer_status: str = models.FloatField("Текущая занятость", default=0)
    qrqode = models.FileField(verbose_name="QR код", upload_to="qr", default=None, null=True, blank=True)

    def __str__(self):
        return self.user_name
    
    @property
    def qrqode_display(self):
        if self.qrqode:
            return mark_safe(
                f'<img src="{self.qrqode.url}" alt="{self.user_name}" width="200" height="200">')
        return ""


