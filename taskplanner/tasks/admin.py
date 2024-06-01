from django.contrib import admin
from .models import TaskModel

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'due_date', 'completed', 'performer')
