from django.contrib import admin
from task.models import *
from rangefilter.filters import NumericRangeFilterBuilder
from import_export.admin import ExportActionMixin



class MyAdminSite(admin.AdminSite):
    site_header = "Информация о проектах"


task_admin = MyAdminSite(name="task-admin")

class EventInline(admin.TabularInline):
    model = Events
    fields = ["start_time", "end_time", "event_status", "creator"]
    readonly_fields = fields[:2]
    extra = False
    show_change_link = True



class TaskDataAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("task_number", "task_name", "status")
    list_display_links = list_display[:2]
    list_filter = (("work_manage", NumericRangeFilterBuilder()),"status", "priority", "task_type",)
    search_fields = ("task_number", "task_name")
    list_select_related = ("project",)
    list_per_page = 50
    list_editable = ("status",)
    search_help_text = "Поиск работает по номеру задачи или ее названию"
    inlines = (EventInline, )
   
class TaskInline(admin.TabularInline):
    model = TaskData
    fields = ["task_name", "status", "priority"]
    readonly_fields = fields
    extra = False
    show_change_link = True

class ProjectAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("project_name",)
    search_fields = ("project_name",)
    search_help_text = "Введите название проекта"
    inlines = (TaskInline, )


class EventsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("start_time", "end_time", "event_status", "creator", )
    list_filter = ("event_status", "creator", )
    date_hierarchy = "start_time"
    
    pass
    
task_admin.register(Project, ProjectAdmin)
task_admin.register(TaskData, TaskDataAdmin)
task_admin.register(Events, EventsAdmin)
