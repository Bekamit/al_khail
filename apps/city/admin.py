from django.utils.safestring import mark_safe
from django.contrib import admin
from service.admin import CustomModelAdmin

from .models import *


@admin.register(City)
class CityAdmin(CustomModelAdmin):
    list_display = ('city_name', 'city_description_preview', 'preview')
    search_fields = ('city_name', 'city_name_ar', 'city_tr', 'city_ru')
    list_filter = ('city_name',)
    readonly_fields = ['preview']

    fieldsets = [
        ('English', {
            'fields': [
                'city_name_en',
                'city_description_en',
                'city_img',
                'preview'
            ],
        }),
        ('Arabic', {
            'fields': [
                'city_name_ar',
                'city_description_ar'
            ],
        }),
        ('Turkish', {
            'fields': [
                'city_name_tr',
                'city_description_tr'
            ],
        }),
        ('Russian', {
            'fields': [
                'city_name_ru',
                'city_description_ru',
            ],
        }),
    ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.city_img.url}", style="max-height: 150px;">')

    def city_description_preview(self, obj):
        return mark_safe(f'<div style="max-height: 150px; overflow: auto">{obj.city_description}</div>')
