from .models import Consultation
from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.analytics.models import CatalogDownloader, Appeal
from service.admin import ReadDeleteModelAdmin


class CatalogDownloaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'role', 'created_at')
    readonly_fields = ('name', 'phone', 'role', 'created_at')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(CatalogDownloader, CatalogDownloaderAdmin)


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


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'city', 'at_date', 'created_at')
    readonly_fields = ('name', 'phone', 'city', 'at_date', 'created_at')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Consultation, ConsultationAdmin)
