from django.contrib import admin
from service.admin import ReadDeleteModelAdmin
from .models import *


@admin.register(Appeal)
class ReadDeleteAppealAdmin(ReadDeleteModelAdmin):
    fields = ('name', 'phone', 'lang', 'is_for_purchase')
    list_filter = ('created_at', 'lang', 'is_for_purchase')
