from modeltranslation.translator import translator, TranslationOptions
from .models import Company


class CompanyTranslationOptions(TranslationOptions):
    fields = ('mission',
              'history',
              'company',)
    required_languages = ('en', )


translator.register(Company, CompanyTranslationOptions)
