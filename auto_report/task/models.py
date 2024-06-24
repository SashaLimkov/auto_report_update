from django.db import models
from backend.models import TimeBasedModel


class Project(TimeBasedModel):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering=["-project_name"]
        
        
    project_name: str = models.CharField(verbose_name="Название проекта", max_length=255)

    def __str__(self):
        return self.project_name


class TaskData(TimeBasedModel):
    class Meta:
        verbose_name = "Текущая задача"
        verbose_name_plural = "Список задач"
        ordering = ["-task_number"]
    
    class Status(models.TextChoices):
        NEW = "1", "Новая"
        IN_PROCESS = "2", "В работе"
        FEED_BACK = "3", "Обратная связь"
        SOLVED = "4", "Решена"
        CLOSED = "5", "Закрыта"
        PAUSED = "6", "Пауза"
        REJECTED = "7", "Отклонена"
        
    
    project: str = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name="tasks",
        verbose_name="Проект",
    )
    task_number: str = models.IntegerField("Номер задачи", null=True, blank=True) 
    status: str = models.CharField("Статус выполнения задачи", max_length=1, choices=Status.choices, null=True, blank=True)
    priority: str = models.CharField("Приоритет задачи", max_length=128)
    ready: str = models.CharField("Статус готовности задачи",max_length=128)
    time_manage: float = models.IntegerField("Оценка временных затрат")
    work_manage: float = models.IntegerField("Трудозатраты")
    initiator: str = models.CharField(
        "От кого был создан запрос", max_length=128, null=True, blank=True, default=None
    )
    description: str = models.TextField(
        "Описание", max_length=255, null=True, blank=True, default=None
    )
    task_type: str = models.CharField("Тип задачи", max_length=128)

    def __str__(self):
        return self.project_name.__str__()


class Events(TimeBasedModel):
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ["start_time"]

    task_info: str = models.ForeignKey(
        TaskData,
        on_delete=models.SET_NULL,
        null=True,
        related_name="event_name",
        verbose_name="Задача"
    )
    start_time: str = models.DateTimeField("Время начала работы")
    end_time: str = models.DateTimeField("Время окончания работы", blank=True, null=True)
    comments: str = models.TextField(
        "Комментарий разработчика", max_length=2048,
        default=None, null=True, blank=True
    )
    ready_status: str = models.CharField("Event - статус", max_length=128)

    def __str__(self):
        return self.task_info.__str__()
