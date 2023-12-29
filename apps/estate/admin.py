from django.contrib import admin
from .models import EstateType, Estate, EstateImage




class EstateImageInline(admin.TabularInline):
    model = EstateImage
    extra = 1


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'developer',
                    'area',
                    'district',
                    'description',
                    'estate_type',
                    'city',
                    'is_secondary',
                    'create_at')
    search_fields = ('name', 'developer', 'district', 'estate_type__type', 'city__city_name_en')
    list_filter = ('estate_type', 'city', 'is_secondary')
    fieldsets = [
        ('English', {
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
        ('Arabic', {
            'fields': [
                'name_ar',
                'developer_ar',
                'district_ar',
                'description_ar',
            ]
        }),
        ('Turkish', {
            'fields': [
                'name_tr',
                'developer_tr',
                'district_tr',
                'description_tr',
            ]
        }),
        ('Russian', {
            'fields': [
                'name_ru',
                'developer_ru',
                'district_ru',
                'description_ru',
            ],
        })
    ]
    inlines = [EstateImageInline]


@admin.register(EstateType)
class EstateTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)
    # list_filter = ('estate_type', 'city', 'is_secondary')
    fieldsets = [
        ('English', {
            'fields': [
                'type',
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
