from django.contrib import admin
from task.admin import task_admin, EventInline
from employers.models import Employer
from rangefilter.filters import NumericRangeFilterBuilder
from import_export.admin import ExportActionMixin
from aiogram.utils.deep_linking import encode_payload
from employers.utils import qr
import os
from auto_report.settings import BASE_DIR
from django.core.files import File
# class EmployerInLine(admin.TabularInline):
#     model = Employer
#     fields = []
#     pass

class EmployerAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("user_name", "start_time", "end_time", "employer_status","qrqode_display" )
    list_filter = ("start_time", ("employer_status", NumericRangeFilterBuilder()))
    search_fields = ("user_name", )
    inlines = (EventInline, )
    actions  =  (
        "create_qr",
    )
    
    def create_qr(self, request, queryset):
        for user in queryset.all():
            redmine_id = user.redmine_id
            link = f"https://t.me/testing_funcs_bot?start={encode_payload(redmine_id)}"
            file_path = qr.generate_qr(link=link, name=f"{user.user_name}")
            path = os.path.join(BASE_DIR, file_path)
            with open(path,  "rb") as f:
                user.qrqode.save(file_path, File(f))
                user.save()
            try:
                os.remove(path=path) 
            except:
                pass
    
    def qrqode_display(self, item):
        return item.qrqode_display

    qrqode_display.short_description = 'qr'
    qrqode_display.allow_tags = True
    create_qr.short_description =  "Сгенерировать QR code"

# @receiver(post_save, sender=Employee)
# def update_invite_link(sender, instance, **kwargs):
#     if not instance.invite_link:
#         pk = instance.pk
#         link = "https://t.me/icdc_pcr_notifier_bot?start="
#         link += encode_payload(f"{pk}")
#         instance.invite_link = link
#         file_path = generate_qr(link=link, name=f"{instance.name}_{pk}")
#         pathh = os.path.join(BASE_DIR, file_path)
#         print(pathh)
#         with open(pathh, "rb") as f:
#             instance.qrqode.save(
#                 file_path,
#                 File(f))
#         instance.save()
#         try:
#             os.remove(path=pathh)
#         except:
#             pass
    
#     department = instance.department
#     if department:
#         all_employers = Employee.objects.filter(department=department)
#         dep_all_notes = all_employers.aggregate(Sum("total_count"))["total_count__sum"]
#         dep_lost_notes = all_employers.aggregate(Sum("count_of_lost_deadline"))[
#             "count_of_lost_deadline__sum"]
#         not_filled = all_employers.aggregate(Sum("not_filled_now"))["not_filled_now__sum"]
#         ill_found_count = all_employers.aggregate(Sum("ill_found_count"))["ill_found_count__sum"]
#         department.count_deadline_lost = dep_lost_notes
#         department.total_notes_count = dep_all_notes
#         department.count_not_filled_notes = not_filled
#         department.ill_found_count = ill_found_count
#         department.save()
task_admin.register(Employer, EmployerAdmin)
