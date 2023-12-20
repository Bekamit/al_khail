from modeltranslation.translator import translator, TranslationOptions
from .models import Estate, EstateType, City


class EstateTranslationOptions(TranslationOptions):
    fields = ('name', 'developer', 'district', 'description')


class CityTranslationOptions(TranslationOptions):
    fields = ('city_name', 'city_description')


class EstateTypeTranslationOptions(TranslationOptions):
    fields = ('type',)


translator.register(Estate, EstateTranslationOptions)
translator.register(City, CityTranslationOptions)
translator.register(EstateType, EstateTypeTranslationOptions)
