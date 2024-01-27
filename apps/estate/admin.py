from django.utils.safestring import mark_safe

from django.contrib import admin
from tinymce.widgets import TinyMCE

from service.admin import CustomModelAdmin
from .models import EstateType, Estate, EstateImage


class EstateImageInline(admin.TabularInline):
    model = EstateImage
    extra = 1


@admin.register(Estate)
class EstateAdmin(CustomModelAdmin):
    list_display = ('title',
                    'project',
                    'area',
                    'estate_type',
                    'city',
                    'visits',
                    'preview')
    search_fields = ('project__name', 'title', 'estate_type__type_en', 'city__city_name_en')
    list_filter = ('city__city_name', 'project__name', 'estate_type__type', 'is_secondary')
    fieldsets = [
        ('English', {
            'fields': [
                'project',
                'title_en',
                'area',
                'description_en',
                'price_usd',
                'estate_type',
                'city',
                'is_secondary',
            ],
        }),
        ('Arabic', {
            'fields': [
                'title_ar',
                'description_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'title_tr',
                'description_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'title_ru',
                'description_ru',
            ],
        })
    ]
    inlines = [EstateImageInline]

    def preview(self, obj):
        return mark_safe(f'<button class="btn btn-primary" style=margin-left: 15px;">look up</button>')


@admin.register(EstateType)
class EstateTypeAdmin(CustomModelAdmin):
    list_display = ('type',)
    search_fields = ('type', 'type_ar', 'type_tr', 'type_ru')
    fieldsets = [
        ('English', {
            'fields': [
                'type_en',
            ],
        }),
        ('Arabic', {
            'fields': [
                'type_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'type_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'type_ru',
            ],
        })
    ]
