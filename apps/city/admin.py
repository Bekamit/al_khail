from django.contrib import admin
from .models import *


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'city_description', 'city_img')
    search_fields = ('city_name', 'city_description')
    list_filter = ('city_name', 'city_description')

    fieldsets = [
        ('English', {
            'fields': [
                'city_name',
                'city_description',
                'city_img',
            ],
        }),
        ('Russian', {
            'fields': [
                'city_name_ru',
                'city_description_ru',
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
    ]
