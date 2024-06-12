from django.contrib import admin
from .models import BoardModel


@admin.register(BoardModel)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'progress')
