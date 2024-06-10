from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["User","task_name","deadline","task_status"]

admin.site.register(Task,TaskAdmin)