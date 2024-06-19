from django.db import models
from auto_report.backend.models import TimeBasedModel


class Project(TimeBasedModel):
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Все задачи"
        pass

    project_name: str = models.CharField(verbose_name="Название задачи", max_length=255)

    def __str__(self):
        return self.project_name


class TaskData(TimeBasedModel):
    class Meta:
        verbose_name = "Текущая задача"
        verbose_name_plural = "Список задач"
        ordering = ["-project_name"]
        pass

    project_name: str = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name="task_name",
        verbose_name="Название задачи",
    )
    status: str = models.CharField("Статус выполнения задачи")
    priority: str = models.CharField("Приоритет задачи")
    ready: str = models.CharField("Статус готовности задачи")
    time_manage: float = models.IntegerField("Оценка временных затрат")
    work_manage: float = models.IntegerField("Трудозатраты")
    initiator: str = models.CharField(
        "От кого был создан запрос", max_length=128, null=True, blank=True, default=None
    )
    description: str = models.TextField(
        "Описание", max_length=255, null=True, blank=True, default=None
    )
    task_type: str = models.CharField("Тип задачи")

    def __str__(self):
        return self.project_name
