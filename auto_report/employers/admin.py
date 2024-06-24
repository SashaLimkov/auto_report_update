from django.contrib import admin
from task.admin import task_admin, EventInline
from employers.models import Employer
from rangefilter.filters import NumericRangeFilterBuilder
from import_export.admin import ExportActionMixin


# class EmployerInLine(admin.TabularInline):
#     model = Employer
#     fields = []
#     pass

class EmployerAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("user_name", "tg_urls", "start_time", "end_time", "employer_status", )
    list_filter = ("user_name", "employer_status", )
    search_fields = ("user_name", )
    inlines = (EventInline, )
    pass


task_admin.register(Employer, EmployerAdmin)
