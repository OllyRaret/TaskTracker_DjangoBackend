from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

@admin.register(UserModel)
class _UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
