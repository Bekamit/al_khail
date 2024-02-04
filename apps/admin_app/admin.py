from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'language', 'password')


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
