from modeltranslation.translator import translator, TranslationOptions
from .models import Header, Body, Form, Footer, Error404


class HeaderTranslationOptions(TranslationOptions):
    fields = ('city',
              'all_real_estates',
              'place_ad',
              'about_us',)
    required_languages = ('en',)


class BodyTranslationOptions(TranslationOptions):
    fields = ('main',
              'search',
              'slogan',
              'see_real_estates',
              'city',
              'estate_type',
              'popular',
              'new_add',
              'all',
              'show_result',
              'we_have',
              'benefits',
              'wide_selection',
              'confidentiality',
              'exclusive_offers',
              'feedback',
              'view_more',
              'furnished',
              'completion',
              'price_at',
              'catalog',
              'features_and_amenities',
              'description',
              'similar_properties',
              'mission_and_history',
              'mission',
              'history',
              'company',)
    required_languages = ('en',)


class FooterTranslationOptions(TranslationOptions):
    fields = ('contact_us',
              'cities',
              'estate_types',
              'pages',)
    required_languages = ('en',)


class FormTranslationOptions(TranslationOptions):
    fields = ('contact_us',
              'any_question',
              'leave_your_contacts',
              'submit_application',
              'fill_form',
              'sell_with_us',
              'download_catalog',
              'your_name',
              'your_email',
              'phone_number',
              'your_city',
              'date',
              'send',
              'close',
              'download',
              'select_role',
              'agent',
              'buyer',
              'exploring',)
    required_languages = ('en',)


class Error404TranslationOptions(TranslationOptions):
    fields = ('not_found',
              'error_description',)
    required_languages = ('en',)


translator.register(Header, HeaderTranslationOptions)
translator.register(Body, BodyTranslationOptions)
translator.register(Footer, FooterTranslationOptions)
translator.register(Form, FormTranslationOptions)
translator.register(Error404, Error404TranslationOptions)
