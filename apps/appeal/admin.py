from django.contrib import admin
from django.utils.safestring import mark_safe

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
    list_display = ('date', 'name', 'want_to', 'estate_link', 'phone', 'is_send')
    fields = ('name', 'estate_link', 'phone', 'lang', 'want_to')
    list_filter = ('created_at', 'lang', 'is_for_purchase', 'estate')

    def want_to(self, obj):
        return f'{"BUY" if obj.is_for_purchase else "SELL"}'

    def date(self, obj):
        return f'#{obj.pk} | {obj.created_at.strftime("%Y-%m-%d, %H:%M")}'

    def estate_link(self, obj):
        if obj.estate:
            return mark_safe(f'<a href="#">path/to/estate/{obj.estate.pk}/</a>')
