from modeltranslation.translator import translator, TranslationOptions
from .models import Estate, EstateType


class EstateTranslationOptions(TranslationOptions):
    fields = ('name',
              'developer',
              'district',
              'description',)
              # 'price',
              # 'currency')


class EstateTypeTranslationOptions(TranslationOptions):
    fields = ('type',)


translator.register(Estate, EstateTranslationOptions)
translator.register(EstateType, EstateTypeTranslationOptions)
