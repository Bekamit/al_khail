from django.contrib import admin
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'about', 'phone', 'email', 'company_img')
    search_fields = ('company_name', 'about', 'phone', 'email')
    list_filter = ('company_name', 'about', 'phone', 'email')

    fieldsets = [
        ('English', {
            'fields': [
                'company_name',
                'about',
                'company_img'
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
