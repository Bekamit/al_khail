
from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import *


# class AppealAdminInline(TabularInline):
#     extra = 1
#     model = Appeal

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    fields = ('name', 'phone', 'lang', 'is_for_purchase')