from django.contrib import admin
from service.admin import CustomModelAdmin

from .models import Header, Body, Form, DefaultValue


@admin.register(Header)
class StaticDataAdmin(CustomModelAdmin):
    fieldsets = [
        ('English', {
            'fields': [
                'buy_en',
                'all_properties_en',
                'place_ad_en',
                'contact_as_en',
                'slogan_en',
                'search_en',
                'city_en',
                'estate_type_en',
                'show_result_en',
                'filter_en',
                'all_en',
                'popular_en',
                'new_add_en'
            ],
        }),
        ('Arabic', {
            'fields': [
                'buy_ar',
                'all_properties_ar',
                'place_ad_ar',
                'contact_as_ar',
                'slogan_ar',
                'search_ar',
                'city_ar',
                'estate_type_ar',
                'show_result_ar',
                'filter_ar',
                'all_ar',
                'popular_ar',
                'new_add_ar'
            ],
        }),
        ('Turkish', {
            'fields': [
                'buy_tr',
                'all_properties_tr',
                'place_ad_tr',
                'contact_as_tr',
                'slogan_tr',
                'search_tr',
                'city_tr',
                'estate_type_tr',
                'show_result_tr',
                'filter_tr',
                'all_tr',
                'popular_tr',
                'new_add_tr'
            ],
        }),
        ('Russian', {
            'fields': [
                'buy_ru',
                'all_properties_ru',
                'place_ad_ru',
                'contact_as_ru',
                'slogan_ru',
                'search_ru',
                'city_ru',
                'estate_type_ru',
                'show_result_ru',
                'filter_ru',
                'all_ru',
                'popular_ru',
                'new_add_ru'
            ],
        })
    ]


@admin.register(Body)
class StaticDataAdmin(CustomModelAdmin):
    fieldsets = [
        ('English', {
            'fields': [
                'property_en',
                'about_company_en',
                'why_en',
                'advantages_en',
                'all_properties_en',
                'view_more_en',
                'listing_details_en',
                'facilities_en',
                'download_catalog_en',
                'description_en',
                'you_might_like_en'
            ],
        }),
        ('Arabic', {
            'fields': [
                'property_ar',
                'about_company_ar',
                'why_ar',
                'advantages_ar',
                'all_properties_ar',
                'view_more_ar',
                'listing_details_ar',
                'facilities_ar',
                'download_catalog_ar',
                'description_ar',
                'you_might_like_ar'
            ],
        }),
        ('Turkish', {
            'fields': [
                'property_tr',
                'about_company_tr',
                'why_tr',
                'advantages_tr',
                'all_properties_tr',
                'view_more_tr',
                'listing_details_tr',
                'facilities_tr',
                'download_catalog_tr',
                'description_tr',
                'you_might_like_tr'
            ],
        }),
        ('Russian', {
            'fields': [
                'property_ru',
                'about_company_ru',
                'why_ru',
                'advantages_ru',
                'all_properties_ru',
                'view_more_ru',
                'listing_details_ru',
                'facilities_ru',
                'download_catalog_ru',
                'description_ru',
                'you_might_like_ru'
            ],
        })
    ]


@admin.register(Form)
class StaticDataAdmin(CustomModelAdmin):
    fieldsets = [
        ('English', {
            'fields': [
                'callback_form_title_en',
                'sell_form_title_en',
                'download_catalog_form_title_en',
                'form_description_en',
                'your_name_en',
                'your_email_en',
                'your_phone_en',
                'your_city_en',
                'at_date_en',
                'send_en',
                'role_en',
                'agent_en',
                'buyer_en',
                'exploring_en',
                'download_en'
            ],
        }),
        ('Arabic', {
            'fields': [
                'callback_form_title_ar',
                'sell_form_title_ar',
                'download_catalog_form_title_ar',
                'form_description_ar',
                'your_name_ar',
                'your_email_ar',
                'your_phone_ar',
                'your_city_ar',
                'at_date_ar',
                'send_ar',
                'role_ar',
                'agent_ar',
                'buyer_ar',
                'exploring_ar',
                'download_ar'
            ],
        }),
        ('Turkish', {
            'fields': [
                'callback_form_title_tr',
                'sell_form_title_tr',
                'download_catalog_form_title_tr',
                'form_description_tr',
                'your_name_tr',
                'your_email_tr',
                'your_phone_tr',
                'your_city_tr',
                'at_date_tr',
                'send_tr',
                'role_tr',
                'agent_tr',
                'buyer_tr',
                'exploring_tr',
                'download_tr'
            ],
        }),
        ('Russian', {
            'fields': [
                'callback_form_title_ru',
                'sell_form_title_ru',
                'download_catalog_form_title_ru',
                'form_description_ru',
                'your_name_ru',
                'your_email_ru',
                'your_phone_ru',
                'your_city_ru',
                'at_date_ru',
                'send_ru',
                'role_ru',
                'agent_ru',
                'buyer_ru',
                'exploring_ru',
                'download_ru'
            ],
        })
    ]


@admin.register(DefaultValue)
class StaticDataAdmin(admin.ModelAdmin):
    ...
