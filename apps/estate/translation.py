from modeltranslation.translator import translator, TranslationOptions
from .models import Estate, EstateType


class EstateTranslationOptions(TranslationOptions):
    fields = ('title',
              'description',)
    required_languages = ('en',)


class EstateTypeTranslationOptions(TranslationOptions):
    fields = ('type',)
    required_languages = ('en',)


translator.register(Estate, EstateTranslationOptions)
translator.register(EstateType, EstateTypeTranslationOptions)
