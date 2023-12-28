from django.contrib import admin
from .models import EstateType, Estate, EstateImage

# class EstateTypeInline(admin.TabularInline):
#     model = EstateType
#     extra = 1

class EstateImageInline(admin.TabularInline):
    model = EstateImage
    extra = 1

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer', 'area', 'district', 'description', 'estate_type', 'city', 'is_secondary', 'create_at')
    search_fields = ('name', 'developer', 'district', 'estate_type__type', 'city__city_name_en')
    list_filter = ('estate_type', 'city', 'is_secondary')
    fieldsets = [
        (
        'General', {
            'fields': [
                'name',
                'developer',
                'area',
                'district',
                'description',
                'estate_type',
                'city',
                'is_secondary',
            ],
        }),
        ('Russian', {
            'fields': [
                'name_ru',
                'developer_ru',
                'district_ru',
                'description_ru',
            ],
        }),
        ('English', {
            'fields': [
                'name_en',
                'developer_en',
                'district_en',
                'description_en',
            ]
        }),
        ('Arabic', {
            'fields': [
                'name_ar',
                'developer_ar',
                'district_ar',
                'description_ar',
            ]
        }),
        ('Turkic', {
            'fields': [
                'name_tr',
                'developer_tr',
                'district_tr',
                'description_tr',
            ]
        })
    ]
    inlines = [EstateImageInline]


