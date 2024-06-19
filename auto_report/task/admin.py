from django.contrib import admin
from auto_report.task.models import *


class MyAdminSite(admin.AdminSite):
    site_header = "Надстройки"


task_admin = MyAdminSite(name="task-admin")


task_admin.register(Project)
task_admin.register(TaskData)
