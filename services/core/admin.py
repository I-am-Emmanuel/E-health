from django.contrib import admin
from . models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_joined',]