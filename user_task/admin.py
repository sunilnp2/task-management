from django.contrib import admin

from user_task.models import Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'status', 'difficulty', 'created_at']
    search_fields = ['title']
    list_filter = ['status', 'created_by']


admin.site.register(Task, TaskAdmin)
