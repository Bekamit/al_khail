from django.contrib import admin
from service.admin import CustomModelAdmin

from .models import Header, Body, Form, Footer, Error404, DefaultValue


@admin.register(Header)
class HeaderDataAdmin(CustomModelAdmin):
    list_display = ['__str__', 'not_null_fields']
    fieldsets = [
        ('English', {
            'fields': [
                'city_en',
                'all_properties_en',
                'place_ad_en',
                'contact_as_en',
            ],
        }),
        ('Arabic', {
            'fields': [
                'city_ar',
                'all_properties_ar',
                'place_ad_ar',
                'contact_as_ar',
            ],
        }),
        ('Turkish', {
            'fields': [
                'city_tr',
                'all_properties_tr',
                'place_ad_tr',
                'contact_as_tr',
            ],
        }),
        ('Russian', {
            'fields': [
                'city_ru',
                'all_properties_ru',
                'place_ad_ru',
                'contact_as_ru',
            ],
        })
    ]


@admin.register(Body)
class BodyDataAdmin(CustomModelAdmin):
    list_display = ['__str__', 'not_null_fields']
    fieldsets = [
        ('English', {
            'fields': [
                'main_en',
                'search_en',
                'slogan_en',
                'see_real_estates_en',
                'city_en',
                'estate_type_en',
                'popular_en',
                'new_add_en',
                'all_en',
                'show_result_en',
                'we_have_en',
                'benefits_en',
                'wide_selection_en',
                'confidentiality_en',
                'exclusive_offers_en',
                'feedback_en',
                'view_more_en',
                'furnished_en',
                'completion_en',
                'price_at_en',
                'catalog_en',
                'features_and_amenities_en',
                'description_en',
                'similar_properties_en',
                'mission_and_history_en',
                'mission_en',
                'history_en',
                'company_en',
            ],
        }),
        ('Arabic', {
            'fields': [
                'main_ar',
                'search_ar',
                'slogan_ar',
                'see_real_estates_ar',
                'city_ar',
                'estate_type_ar',
                'popular_ar',
                'new_add_ar',
                'all_ar',
                'show_result_ar',
                'we_have_ar',
                'benefits_ar',
                'wide_selection_ar',
                'confidentiality_ar',
                'exclusive_offers_ar',
                'feedback_ar',
                'view_more_ar',
                'furnished_ar',
                'completion_ar',
                'price_at_ar',
                'catalog_ar',
                'features_and_amenities_ar',
                'description_ar',
                'similar_properties_ar',
                'mission_and_history_ar',
                'mission_ar',
                'history_ar',
                'company_ar',
            ],
        }),
        ('Turkish', {
            'fields': [
                'main_tr',
                'search_tr',
                'slogan_tr',
                'see_real_estates_tr',
                'city_tr',
                'estate_type_tr',
                'popular_tr',
                'new_add_tr',
                'all_tr',
                'show_result_tr',
                'we_have_tr',
                'benefits_tr',
                'wide_selection_tr',
                'confidentiality_tr',
                'exclusive_offers_tr',
                'feedback_tr',
                'view_more_tr',
                'furnished_tr',
                'completion_tr',
                'price_at_tr',
                'catalog_tr',
                'features_and_amenities_tr',
                'description_tr',
                'similar_properties_tr',
                'mission_and_history_tr',
                'mission_tr',
                'history_tr',
                'company_tr',
            ],
        }),
        ('Russian', {
            'fields': [
                'main_ru',
                'search_ru',
                'slogan_ru',
                'see_real_estates_ru',
                'city_ru',
                'estate_type_ru',
                'popular_ru',
                'new_add_ru',
                'all_ru',
                'show_result_ru',
                'we_have_ru',
                'benefits_ru',
                'wide_selection_ru',
                'confidentiality_ru',
                'exclusive_offers_ru',
                'feedback_ru',
                'view_more_ru',
                'furnished_ru',
                'completion_ru',
                'price_at_ru',
                'catalog_ru',
                'features_and_amenities_ru',
                'description_ru',
                'similar_properties_ru',
                'mission_and_history_ru',
                'mission_ru',
                'history_ru',
                'company_ru',
            ],
        })
    ]


@admin.register(Form)
class FormDataAdmin(CustomModelAdmin):
    list_display = ['__str__', 'not_null_fields']
    fieldsets = [
        ('English', {
            'fields': [
                'contact_us_en',
                'any_question_en',
                'leave_your_contacts_en',
                'submit_application_en',
                'fill_form_en',
                'sell_with_us_en',
                'download_catalog_en',
                'your_name_en',
                'your_email_en',
                'phone_number_en',
                'your_city_en',
                'date_en',
                'send_en',
                'close_en',
                'download_en',
                'select_role_en',
                'agent_en',
                'buyer_en',
                'exploring_en',
            ],
        }),
        ('Arabic', {
            'fields': [
                'contact_us_ar',
                'any_question_ar',
                'leave_your_contacts_ar',
                'submit_application_ar',
                'fill_form_ar',
                'sell_with_us_ar',
                'download_catalog_ar',
                'your_name_ar',
                'your_email_ar',
                'phone_number_ar',
                'your_city_ar',
                'date_ar',
                'send_ar',
                'close_ar',
                'download_ar',
                'select_role_ar',
                'agent_ar',
                'buyer_ar',
                'exploring_ar',
            ],
        }),
        ('Turkish', {
            'fields': [
                'contact_us_tr',
                'any_question_tr',
                'leave_your_contacts_tr',
                'submit_application_tr',
                'fill_form_tr',
                'sell_with_us_tr',
                'download_catalog_tr',
                'your_name_tr',
                'your_email_tr',
                'phone_number_tr',
                'your_city_tr',
                'date_tr',
                'send_tr',
                'close_tr',
                'download_tr',
                'select_role_tr',
                'agent_tr',
                'buyer_tr',
                'exploring_tr',
            ],
        }),
        ('Russian', {
            'fields': [
                'contact_us_ru',
                'any_question_ru',
                'leave_your_contacts_ru',
                'submit_application_ru',
                'fill_form_ru',
                'sell_with_us_ru',
                'download_catalog_ru',
                'your_name_ru',
                'your_email_ru',
                'phone_number_ru',
                'your_city_ru',
                'date_ru',
                'send_ru',
                'close_ru',
                'download_ru',
                'select_role_ru',
                'agent_ru',
                'buyer_ru',
                'exploring_ru',
            ],
        })
    ]


@admin.register(Footer)
class FooterDataAdmin(CustomModelAdmin):
    list_display = ['__str__', 'not_null_fields']
    fieldsets = [
        ('English', {
            'fields': [
                'contact_us_en',
                'cities_en',
                'estate_types_en',
                'pages_en',
            ],
        }),

        ('Arabic', {
            'fields': [
                'contact_us_ar',
                'cities_ar',
                'estate_types_ar',
                'pages_ar',
            ],
        }),
        ('Turkish', {
            'fields': [
                'contact_us_tr',
                'cities_tr',
                'estate_types_tr',
                'pages_tr',
            ],
        }),
        ('Russian', {
            'fields': [
                'contact_us_ru',
                'cities_ru',
                'estate_types_ru',
                'pages_ru',
            ],
        })
    ]


@admin.register(Error404)
class ErrorAdmin(CustomModelAdmin):
    list_display = ['__str__', 'not_null_fields']
    fieldsets = [
        ('English', {
            'fields': [
                'not_found_en',
                'error_description_en',
            ],
        }),
        ('Arabic', {
            'fields': [
                'not_found_ar',
                'error_description_ar',
            ],
        }),
        ('Turkish', {
            'fields': [
                'not_found_tr',
                'error_description_tr',
            ],
        }),
        ('Russian', {
            'fields': [
                'not_found_ru',
                'error_description_ru',
            ],
        })
    ]


@admin.register(DefaultValue)
class DefaultValueAdmin(CustomModelAdmin):
    list_display = ['__str__', 'not_null_fields']
    ...
