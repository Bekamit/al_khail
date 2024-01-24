from modeltranslation.translator import translator, TranslationOptions
from .models import Company


class CompanyTranslationOptions(TranslationOptions):
    fields = ('about',)


translator.register(Company, CompanyTranslationOptions)
