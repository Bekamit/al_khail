from modeltranslation.translator import translator, TranslationOptions
from .models import Company


class CompanyTranslationOptions(TranslationOptions):
    fields = ('company_name',
              'about',)


translator.register(Company, CompanyTranslationOptions)
