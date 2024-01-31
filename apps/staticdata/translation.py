from modeltranslation.translator import translator, TranslationOptions
from .models import Header, Body, Form, Footer


class HeaderTranslationOptions(TranslationOptions):
    fields = ('buy',
              'all_properties',
              'place_ad',
              'contact_as',
              'slogan',
              'search',
              'city',
              'estate_type',
              'show_result',
              'filter',
              'all',
              'popular',
              'new_add',)
    required_languages = ('en',)


class BodyTranslationOptions(TranslationOptions):
    fields = ('property',
              'about_company',
              'why',
              'advantages',
              'all_properties',
              'view_more',
              'listing_details',
              'facilities',
              'download_catalog',
              'description',
              'you_might_like',)
    required_languages = ('en',)


class FormTranslationOptions(TranslationOptions):
    fields = ('callback_form_title',
              'sell_form_title',
              'download_catalog_form_title',
              'form_description',
              'your_name',
              'your_email',
              'your_phone',
              'your_city',
              'at_date',
              'send',
              'role',
              'agent',
              'buyer',
              'exploring',
              'download',)
    required_languages = ('en',)


translator.register(Header, HeaderTranslationOptions)
translator.register(Body, BodyTranslationOptions)
translator.register(Form, FormTranslationOptions)
