from django.contrib import admin
from task.admin import task_admin
from employers.models import Employer


task_admin.register(Employer)
