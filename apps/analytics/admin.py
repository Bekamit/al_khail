from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.analytics.models import CatalogDownloader, Appeal
from service.admin import ReadDeleteModelAdmin


@admin.register(CatalogDownloader)
class ReadDeleteCatalogDownloaderAdmin(ReadDeleteModelAdmin):
    list_display = ('date', 'name', 'role', 'email')
    fields = ('name', 'email', 'phone', 'role', 'date')
    list_filter = ('created_at', 'role',)


@admin.register(Appeal)
class ReadDeleteAppealAdmin(ReadDeleteModelAdmin):
    list_display = ('date', 'name', 'want_to', 'estate_link', 'phone', 'is_send')
    fields = ('name', 'estate_link', 'phone', 'lang', 'want_to')
    list_filter = ('created_at', 'lang', 'is_for_purchase', 'estate')

    def want_to(self, obj):
        return f'{"BUY" if obj.is_for_purchase else "SELL"}'

    def estate_link(self, obj):
        if obj.estate:
            return mark_safe(f'<a href="#">path/to/estate/{obj.estate.pk}/</a>')
