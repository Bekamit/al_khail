from django.contrib import admin
from django.db import models


class CustomModelAdmin(admin.ModelAdmin):
       class Media:
        css = {
            'all': ('css/admin.css',),
        }


class ReadDeleteModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]
