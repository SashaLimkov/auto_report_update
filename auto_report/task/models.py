from django.db import models
from backend.models import TimeBasedModel
from employers.models import Employer


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
    
    class Priority(models.TextChoices):
        LOW = "1", "Низкий"
        MEDIUM = "2", "Нормальный"
        HIGH = "3", "Высокий"
        IMMEDIATLY = "4", "Немедленный"
        QUICKLY = "5", "Срочно"
        
    class Ready(models.TextChoices):
        ZERO = "1", "0%"
        TEN = "2", "10%"
        TWENTY = "3", "20%"
        THIRTY = "4", "30%"
        FORTY = "5", "40%"
        FIFTY = "6", "50%"
        SIXTY = "7", "60"
        SEVENTY = "8", "70%"
        EIGHTY = "9", "80%"
        NINTY = "10", "90%"
        HUNDRED = "11", "100%"
        
      
    class TaskType(models.TextChoices):
        ANALYS = "1", "Анализ"
        MODIFICATIONS = "2", "Доработка"
        DEV_TASK = "3", "Задание разработчику"
        RESEARCH = "4", "Изучение"
        CONSULTATION = "5", "Консультация" 
        ERROR = "6", "Ошибка"
        SOFT_ERROR = "7", "Ошибка ПО"
        USER_ERROR = "8", "Ошибка пользователя"
        SUPPORT = "9", "Поддержка"
        SOFT_SETTINGS = "10", "ПО Настройка"
        SOFT_SETUP = "11", "ПО Установка"
        DEVELOPMENT = "12", "Разработка"
        CONCEPT = "13", "Концепт"
        MEETING = "14", "Совещание"
        TASK_FORM = "15", "Формирование ТЗ"
        INTEGRATION = "16", "Внедрение"
 
 
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
    task_name: str = models.CharField("Название задачи", max_length=255, null=True, blank=True)
    status: str = models.CharField("Статус выполнения задачи", max_length=1, choices=Status.choices, null=True, blank=True)
    priority: str = models.CharField("Приоритет задачи", max_length=1, choices=Priority.choices, null=True, blank=True)
    ready: str = models.CharField("Статус готовности задачи", max_length=2, choices=Ready.choices, null=True, blank=True)
    time_manage: float = models.IntegerField("Оценка временных затрат")
    work_manage: float = models.IntegerField("Трудозатраты")
    initiator: str = models.CharField(
        "От кого был создан запрос", max_length=128, null=True, blank=True, default=None
    )
    description: str = models.TextField(
        "Описание", max_length=255, null=True, blank=True, default=None
    )
    task_type: str = models.CharField("Тип задачи", max_length=2, choices=TaskType.choices, null=True, blank=True)

    def __str__(self):
        return f"№{self.task_number} {self.task_name}"


class Events(TimeBasedModel):
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ["start_time"]
        
    class EventStatus(models.TextChoices):
        PROECTING = "1", "Проектирование"
        DEVELOPING = "2", "Разработка"
        TESTING = "3", "Тестирование"
        RESEARCH = "4", "Изучение"
        REGISTRATION = "5", "Оформление"


    task_info: str = models.ForeignKey(
        TaskData,
        on_delete=models.SET_NULL,
        null=True,
        related_name="event_name",
        verbose_name="Задача"
    )
    creator: str = models.ForeignKey(
        Employer,
        on_delete=models.SET_NULL,
        null=True,
        related_name="Разработчик",
        verbose_name="Работник"  
    )
    start_time: str = models.DateTimeField("Время начала работы")
    end_time: str = models.DateTimeField("Время окончания работы", blank=True, null=True)
    comments: str = models.TextField(
        "Комментарий разработчика", max_length=2048,
        default=None, null=True, blank=True
    )
    event_status: str = models.CharField("Event - статус", max_length=1, choices=EventStatus.choices, null=True, blank=True)

    def __str__(self):
        return self.task_info.__str__()
