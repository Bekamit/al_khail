from modeltranslation.translator import translator, TranslationOptions
from .models import City

class CityTranslationOptions(TranslationOptions):
    fields = ('city_name', 'city_description')


translator.register(City, CityTranslationOptions)
