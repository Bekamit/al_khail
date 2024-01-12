from django.contrib import admin

from .models import *


class ReadDeleteModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]


@admin.register(Appeal)
class ReadDeleteAppealAdmin(ReadDeleteModelAdmin):
    fields = ('name', 'phone', 'lang', 'is_for_purchase')
    list_filter = ('created_at', 'lang', 'is_for_purchase')
