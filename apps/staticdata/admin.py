from django.contrib import admin
from .models import StaticData


@admin.register(StaticData)
class StaticDataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('English', {
            'fields': [
                'field1_en',
                'field2_en',
                'default_image',

            ]
        }),
        ('Arabic', {
            'fields': [
                'field1_ar',
                'field2_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'field1_tr',
                'field2_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'field1_ru',
                'field2_ru',
            ]
        })
    ]

    class Media:
        css = {
            'all': ('css/admin.css',),
        }
