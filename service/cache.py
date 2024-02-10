from django.core.cache import cache
from core.settings.base import MODELTRANSLATION_LANGUAGES


class CustomCache:
    """
    Class CustomCache get one parameter: languages (tuple of languages, srt like `__all__` or None).
    Put queryset for all languages in cache for time witch setting in REST_FRAMEWORK Settings.
    Return queryset from cache if it is, or add queryset in cache if it is not.
    """

    def __init__(self, cache_language):
        self.languages = self.get_cache_language(cache_language)

    @staticmethod
    def get_cache_language(languages):
        if isinstance(languages, str) and languages == '__all__':
            return MODELTRANSLATION_LANGUAGES

        elif isinstance(languages, tuple):
            if all([lang in MODELTRANSLATION_LANGUAGES for lang in languages]):
                return languages
        else:
            raise ValueError('`cache_language` can be: None, tuple of languages or `__all__`')
        return None

    def get(self, key, language):
        return cache.get(f'{key}_{language}')

    def set(self, key, language, queryset):
        cache.set(f'{key}_{language}', queryset)
