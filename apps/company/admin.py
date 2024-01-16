from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'email', 'preview')
    readonly_fields = ['preview']

    fieldsets = [
        ('English', {
            'fields': [
                'company_name_en',
                'about_en',
                'email',
                'phone',
                'company_img',
                'preview'

            ]
        }),
        ('Arabic', {
            'fields': [
                'company_name_ar',
                'about_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'company_name_tr',
                'about_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'company_name_ru',
                'about_ru',
            ]
        })
    ]

    class Media:
        css = {
            'all': ('css/admin.css',),
        }

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.company_img.url}", style="max-height: 200px;">')
