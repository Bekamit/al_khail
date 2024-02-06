from django.contrib import admin
from django.db import models

from tinymce.widgets import TinyMCE


class CustomModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin.css',),
        }

    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    # }


class ReadDeleteModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

    def date(self, obj):
        return f'#{obj.pk} | {obj.created_at.strftime("%Y-%m-%d, %H:%M")}'
