from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters
from service.views import CustomListAPIView
from .serializers import CitySerializer, CityValidateSerializer
from .models import City
from Core import settings


class CityListAPIView(CustomListAPIView):
    """
    ##View Class CityListAPIView return collection of cities from model City

    Multilanguage Response! **ACCEPT-LANGUAGE** is a required header attribute
    that determines the language in which the backend will serve the requested data.
    It accepts both browser-set attributes and those overridden by the frontend.
    In the absence of Accept-Language, the backend will return data in default language: `EN`.

    **methods:**
    - GET *return collection of the cities in Arabic, English, Turkish and Russian language*

    **permission:**
    - *AllowAny*
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny]
    response_key = 'cities'
    filter_backends = [filters.SearchFilter]
    search_fields = ['city_name', 'city_name_ar', 'city_name_tr', 'city_name_ru']


class CityCreateAPIView(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityValidateSerializer
    permission_classes = [AllowAny] if settings.DEBUG else [IsAuthenticated]

