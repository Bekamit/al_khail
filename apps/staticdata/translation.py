from modeltranslation.translator import translator, TranslationOptions
from .models import StaticData


class StaticDataTranslationOptions(TranslationOptions):
    fields = ('field1',
              'field2',)
    required_languages = ('en', 'ar', 'tr', 'ru')


translator.register(StaticData, StaticDataTranslationOptions)
