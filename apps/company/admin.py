from django.utils.safestring import mark_safe
from django.contrib import admin

from service.admin import CustomModelAdmin

from .models import *


@admin.register(Company)
class CompanyAdmin(CustomModelAdmin):
    list_display = ('company_name', 'phone', 'email', 'preview')
    readonly_fields = ['preview']

    fieldsets = [
        ('English', {
            'fields': [
                'company_name',
                'about_en',
                'email',
                'phone',
                'company_img',
                'preview'

            ]
        }),
        ('Arabic', {
            'fields': [
                'about_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'about_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'about_ru',
            ]
        })
    ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.company_img.url}", style="max-height: 200px;">')
