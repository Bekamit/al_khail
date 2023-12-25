from rest_framework.generics import GenericAPIView
from django.utils.translation import get_language_from_request
from Core import settings

from service import mixin


class CustomGenericAPIView(GenericAPIView):
    response_key: str = None

    def get_response_key(self):
        if key := self.response_key:
            if not isinstance(key, str):
                raise ValueError('`response_key` must be str only')
            return key
        else:
            return None

    def get_response_language(self):
        if language := get_language_from_request(self.request):
            return language.upper()
        else:
            return settings.MODELTRANSLATION_DEFAULT_LANGUAGE.upper()


class CustomListAPIView(mixin.CustomListModelMixin, CustomGenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
