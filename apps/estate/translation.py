from modeltranslation.translator import translator, TranslationOptions
from .models import Estate, EstateType, Project


class EstateTranslationOptions(TranslationOptions):
    fields = ('title',
              'developer',
              'district',
              'description',)
    required_languages = ('en',)


class EstateTypeTranslationOptions(TranslationOptions):
    fields = ('type',)
    required_languages = ('en',)


translator.register(Estate, EstateTranslationOptions)
translator.register(EstateType, EstateTypeTranslationOptions)
