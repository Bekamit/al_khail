from rest_framework.generics import GenericAPIView
from django.utils.translation import get_language_from_request
from solo.models import SingletonModel

from rest_framework.serializers import Serializer
from modeltranslation.manager import MultilingualQuerySet
from rest_framework.response import Response
from rest_framework import status

from service import mixin, cache
from core.settings.base import MODELTRANSLATION_DEFAULT_LANGUAGE

from apps.estate.models import Estate, EstateType, EstateImage
from apps.project.models import Project, Facilities
from apps.city.models import City

import asyncio
import requests as req
import aiohttp
from random import choice, randint, uniform
from datetime import datetime, timedelta
from parsel import Selector
from io import BytesIO
from django.core.files import File


class CustomGenericAPIView(GenericAPIView):
    response_key: str | None = None
    cache_class: cache.CustomCache | None = None
    cache_language: str | tuple | None = None
    cache_key = str | None

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
            return MODELTRANSLATION_DEFAULT_LANGUAGE.upper()

    def get_multilanguage_response(self, serializer):
        response_key = self.get_response_key()
        if response_key:
            language = self.get_response_language()

            data = {
                "language": language,
                response_key: serializer.data
            }
        else:
            data = serializer.data
        return data

    def get_cache_key(self):
        if key := self.cache_key:
            if not isinstance(key, str):
                raise ValueError('`cache_key` must be str only')
            return key
        else:
            return None

    def filter(self, queryset: MultilingualQuerySet):
        if issubclass(queryset.model, SingletonModel):
            queryset = queryset.first()
        else:
            queryset = queryset.all()
        return queryset

    def get_queryset(self):
        if not self.cache_language and not self.cache_class:
            return self.filter(super().get_queryset())

        _cache = self.cache_class(self.cache_language)
        accept_language = self.get_response_language()
        if accept_language.lower() in _cache.languages:
            key = self.get_cache_key()
            if queryset := _cache.get(key, accept_language):
                return queryset
            else:
                queryset = self.filter(super().get_queryset())
                _cache.set(key, accept_language, queryset)
                return queryset
        else:
            return self.filter(super().get_queryset())


class MultiSerializerGenericAPIView(CustomGenericAPIView):
    method_get_queryset: MultilingualQuerySet | None = None
    method_get_serializer: Serializer | None = None
    method_post_queryset: MultilingualQuerySet | None = None
    method_post_serializer: Serializer | None = None
    response_queryset: MultilingualQuerySet | None = None
    response_serializer: Serializer | None = None

    def get_queryset(self):
        if self.request.method == 'GET':
            return self.filter(self.method_get_queryset)
        if self.request.method == 'POST':
            return self.filter(self.method_post_queryset)
        return self.filter(self.queryset)

    def get_response_queryset(self):
        if not self.response_queryset:
            return self.filter(self.method_get_queryset)
        return self.filter(self.response_queryset)

    def get_serializer_class(self):
        return self.serializer_class if self.serializer_class else None

    def get_serializer(self, *args, **kwargs):
        serializer = self.serializer_class
        if self.request.method == 'GET':
            serializer = self.method_get_serializer
        if self.request.method == 'POST':
            serializer = self.method_post_serializer
        return serializer


class MultiSerializerListCreateAPIView(mixin.CreateModelMixin, MultiSerializerGenericAPIView):

    def send_form(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer()
        data = self.get_multilanguage_response(serializer(queryset))
        return Response(data)

    def get(self, request, *args, **kwargs):
        return self.send_form(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        kwargs.setdefault('context', self.get_serializer_context())

        serializer = serializer(**kwargs, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        queryset = self.get_response_queryset()
        response_serializer = self.response_serializer(queryset)
        data = self.get_multilanguage_response(response_serializer)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomListAPIView(mixin.CustomListModelMixin, CustomGenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomSingletonListAPIView(mixin.CustomSingletonListModelMixin, CustomGenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.first_list(request, *args, **kwargs)


class CustomRetrieveAPIView(mixin.CustomRetrieveMixin, CustomGenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CustomEstateCreateAPIView(mixin.CustomCreateEstateMixin, CustomGenericAPIView):
    city = None

    def get_fake_estate_apartment(self, page) -> dict:
        r = req.get(url=f"https://api.axcapital.ae/api/v2/property/dubai/buy/apartment-for-sale/?limit=50&page={page}")
        response = r.json()
        data: dict = response.get("data")
        return data.get("results") if data.get('next') else {}

    def get_fake_estate_duplex(self) -> dict:
        r = req.get(url="https://api.axcapital.ae/api/v2/property/dubai/buy/duplex-for-sale/?limit=10&page=1")
        response = r.json()
        data: dict = response.get("data")
        return data.get("results") if data.get('count') else {}

    def get_fake_estate_penthouse(self) -> dict:
        r = req.get(url=f"https://api.axcapital.ae/api/v2/property/dubai/buy/penthouse-for-sale/?limit=15&page=1")
        response = r.json()
        data: dict = response.get("data")
        return data.get("results") if data.get('count') else {}

    def get_fake_estate_villa(self):
        r = req.get(url="https://api.axcapital.ae/api/v2/property/dubai/buy/villa-for-sale/?limit=45&page=1")
        response = r.json()
        data: dict = response.get("data")
        return data.get("results") if data.get('count') else {}

    def random_date(self):
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2025, 12, 31)

        random_days = randint(0, (end_date - start_date).days)
        random_time = uniform(0, 1)
        random_datetime = start_date + timedelta(days=random_days, seconds=random_time * 24 * 60 * 60)

        return random_datetime.strftime('%Y-%m-%d')

    def get_cities(self) -> list[City]:
        return City.objects.all()

    def create_facilities(self, facilities: tuple[str, str, str]) -> Facilities | None:
        try:
            obj = Facilities.objects.get(type_en=facilities[0])
        except Facilities.DoesNotExist:
            try:
                obj = Facilities.objects.create(type_en=facilities[0],
                                                type_ar=facilities[1],
                                                type_ru=facilities[2])
            except Exception:
                obj = None
        return obj

    def create_project(self, project_data, facilities: list[Facilities]) -> Project:
        try:
            obj = Project.objects.get(name=project_data.get('name'))
            return obj
        except Project.DoesNotExist:
            try:
                obj = Project.objects.create(**project_data)
                obj.facilities.add(*[value for value in facilities if value])
                obj.save()
                print(f'[FAKE NEWS]: Project `{project_data.get("name")}` created')
            except Exception:
                obj = None
                print(f'[FAKE NEWS]: Project `{project_data.get("name")}` error')
            return obj

    def create_estate_type(self, estate_type_data: str) -> EstateType:
        obj, _ = EstateType.objects.get_or_create(type_en=estate_type_data.lower())
        return obj

    def save_image(self, estate: Estate, images: list):
        for image in images[:10]:
            img = image.get('image').get('jpeg')
            response = req.get(url=img)
            if response.status_code == 200:
                estate_image = EstateImage(estate=estate)
                estate_image.img.save(img.split('/')[-1], File(BytesIO(response.content)))
                estate_image.save()

    def save_data(self, estate_data: dict):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def fetch_data(language, estate_slug):
            url = f"https://www.axcapital.ae/buy/{estate_slug}"
            if language != 'en':
                url = f"https://www.axcapital.ae/{language}/buy/{estate_slug}"

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.text()

        async def main():
            languages = ['en', 'ar', 'ru']
            tasks = []

            for language in languages:
                task = fetch_data(language, estate_data.get('slug'))
                tasks.append(task)

            return await asyncio.gather(*tasks)

        responses = loop.run_until_complete(main())

        tree_en = Selector(text=responses[0])
        tree_ar = Selector(text=responses[1])
        tree_ru = Selector(text=responses[2])

        description_en = tree_en.xpath('//p[@class="mb-11 whitespace-pre-line text-white60"]/text()').extract_first()
        description_ar = tree_ar.xpath('//p[@class="mb-11 whitespace-pre-line text-white60"]/text()').extract_first()
        description_ru = tree_ru.xpath('//p[@class="mb-11 whitespace-pre-line text-white60"]/text()').extract_first()
        facilities_en = tree_en.xpath('//div[@class="flex min-h-[65px] items-center whitespace-pre-wrap '
                                      'border-b-[1px] border-r-[1px] border-borderMain px-6 text-lg text-white"]/span')
        facilities_ar = tree_ar.xpath('//div[@class="flex min-h-[65px] items-center whitespace-pre-wrap '
                                      'border-b-[1px] border-r-[1px] border-borderMain px-6 text-lg text-white"]/span')
        facilities_ru = tree_ru.xpath('//div[@class="flex min-h-[65px] items-center whitespace-pre-wrap '
                                      'border-b-[1px] border-r-[1px] border-borderMain px-6 text-lg text-white"]/span')

        project = {
            "name": estate_data.get('subcommunity'),
            "location": estate_data.get('location'),
            "developer": "null",
            "completion": self.random_date(),
            "is_furnished": estate_data.get('furnished'),
        }

        facilities_en = [f.css('::text').get().lower() for f in facilities_en]
        facilities_ar = [f.css('::text').get().lower() for f in facilities_ar]
        facilities_ru = [f.css('::text').get().lower() for f in facilities_ru]
        facilities = [f for f in zip(facilities_en, facilities_ar, facilities_ru)]
        all_facilities = [self.create_facilities(f) for f in facilities]

        if p := self.create_project(project, all_facilities):

            with open('back_static/default_catalog/01 - Vincitore Dolce Vita - Project Brief.pdf', 'rb') as file:
                pdf = File(file)
                p.pdf_catalog = pdf
                p.save()

            estate_obj = {"title_en": estate_data.get("title"),
                          "title_ar": "يسر GOLDEN HOUSE تقديم هذا العقار في TITLE TEST.",
                          "title_ru": "GOLDEN HOUSE Тестовое название",
                          "project": p,
                          "area": round(estate_data.get("size") / 3.2808, 2),
                          "description_en": description_en,
                          "description_ar": description_ar,
                          "description_ru": description_ru,
                          "price_usd": round(estate_data.get("price") * 0.27),
                          "estate_type": self.create_estate_type(estate_data.get("property_type")),
                          "city": choice(self.cities),
                          "is_secondary": choice((False, True)),
                          "visits": randint(10, 100)}

            estate = Estate.objects.create(**estate_obj)
            images = estate_data.get('image_data')
            self.save_image(estate=estate, images=images)

            print(f'[FAKE NEWS]: Estate `{estate_data.get("title")}` created')
            return estate
        else:
            print(f'[FAKE NEWS]: Estate `{estate_data.get("title")}` error')

    def post(self, request, *args, **kwargs):
        if self.kwargs.get('password') == 12345:

            self.cities = self.get_cities()

            if Estate.objects.all().count() < 1200:
                villas = self.get_fake_estate_villa()
                for villa in villas:
                    self.save_data(villa)

                duplexes = self.get_fake_estate_duplex()
                for duplex in duplexes:
                    self.save_data(duplex)

                penthouses = self.get_fake_estate_penthouse()
                for penthouse in penthouses:
                    self.save_data(penthouse)

                for page in range(1, 12):
                    apartments = self.get_fake_estate_apartment(page)
                    for apartment in apartments:
                        self.save_data(apartment)
                print("[FAKE NEWS]: All fake data created successfully")

        return self.create(request, *args, **kwargs)
