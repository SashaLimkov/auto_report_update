from django.db import models
from backend.models import TimeBasedModel


class Project(TimeBasedModel):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    project_name: str = models.CharField(verbose_name="Название задачи", max_length=255)

    def __str__(self):
        return self.project_name


class TaskData(TimeBasedModel):
    class Meta:
        verbose_name = "Текущая задача"
        verbose_name_plural = "Список задач"
        ordering = ["-project_name"]

    project_name: str = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name="task_name",
        verbose_name="Название проекта",
    )
    status: str = models.CharField("Статус выполнения задачи", max_length=128)
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
        blank=True,
        default=None,
        related_name="event_name",
        verbose_name="Название задачи"
    )
    start_time: str = models.DateTimeField("Время начала работы")
    end_time: str = models.DateTimeField("Время окончания работы")
    comments: str = models.TextField(
        "Комментарий разработчика", max_length=2048,
        default=None, null=True, blank=True
    )
    ready_status: str = models.CharField("Event - статус", max_length=128)

    def __str__(self):
        return self.task_info.__str__()
