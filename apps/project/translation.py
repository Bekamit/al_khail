from modeltranslation.translator import TranslationOptions, translator
from .models import Facilities


class FacilitiesTranslationOptions(TranslationOptions):
    fields = ('type',)
    required_languages = ('en',)


translator.register(Facilities, FacilitiesTranslationOptions)
