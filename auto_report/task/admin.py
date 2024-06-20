from django.contrib import admin
from task.models import *


class MyAdminSite(admin.AdminSite):
    site_header = "Информация о проектах"


task_admin = MyAdminSite(name="task-admin")


task_admin.register(Project)
task_admin.register(TaskData)
task_admin.register(Events)
