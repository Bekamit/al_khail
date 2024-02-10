from django.utils.safestring import mark_safe
from django.contrib import admin

from service.admin import CustomModelAdmin

from .models import *


@admin.register(Company)
class CompanyAdmin(CustomModelAdmin):
    list_display = ('company_name', 'phone', 'email', 'get_logo')
    readonly_fields = ['get_logo']

    fieldsets = [
        ('English', {
            'fields': [
                'company_name',
                'mission_en',
                'history_en',
                'company_en',
                'email',
                'phone',
                'company_img',
                'get_logo'

            ]
        }),
        ('Arabic', {
            'fields': [
                'mission_ar',
                'history_ar',
                'company_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'mission_tr',
                'history_tr',
                'company_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'mission_ru',
                'history_ru',
                'company_ru',
            ]
        })
    ]

    def get_logo(self, obj):
        return mark_safe(f'<img src="{obj.company_img.url}", style="max-height: 200px;">')
    get_logo.short_description = 'logo'
