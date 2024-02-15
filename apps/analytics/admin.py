from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.analytics.models import CatalogDownloader, Appeal
from service.admin import ReadDeleteModelAdmin


@admin.register(CatalogDownloader)
class ReadDeleteCatalogDownloaderAdmin(ReadDeleteModelAdmin):
    list_display = ('date', 'name', 'role', 'email')
    fields = ('name', 'email', 'phone', 'lang', 'role', 'date')
    list_filter = ('created_at', 'role',)


@admin.register(Appeal)
class AppealAdmin(ReadDeleteModelAdmin):
    list_display = ('date', 'name', 'want_to', 'estate_link', 'phone', 'is_send')
    list_filter = ('created_at', 'lang', 'appeal_type', 'estate')

    def want_to(self, obj):
        return obj.appeal_type if obj.appeal_type in ['buy', 'sell', 'consultation'] else 'Unknown'

    def estate_link(self, obj):
        if obj.estate:
            return mark_safe(f'<a href="#">path/to/estate/{obj.estate.pk}/</a>')
        return '-'
