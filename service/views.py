from django.db import transaction
from rest_framework.generics import GenericAPIView
from django.utils.translation import get_language_from_request
from core import settings

from service import mixin

from apps.estate.models import Estate, EstateType, EstateImage
from apps.estate.tests import ESTATE_TYPES
from apps.project.models import Project, Facilities
from apps.city.models import City
from apps.city.tests import CITIES
from requests import request as req
from random import choice, randint, uniform
from datetime import datetime, timedelta
from parsel import Selector
from io import BytesIO
from django.core.files import File


class CustomGenericAPIView(GenericAPIView):
    response_key: str | None = None

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
            return settings.base.MODELTRANSLATION_DEFAULT_LANGUAGE.upper()


class CustomListAPIView(mixin.CustomListModelMixin, CustomGenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomSingletonListAPIView(mixin.CustomSingletonListModelMixin, CustomGenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomRetrieveAPIView(mixin.CustomRetrieveMixin, CustomGenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CustomRetrieveImagesAPIView(mixin.CustomRetrieveEstateImageMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomEstateCreateAPIView(mixin.CustomCreateEstateMixin, CustomGenericAPIView):
    city = None

    def get_fake_estate_apartment(self, page):
        r = req(method="GET",
                url=f"https://api.axcapital.ae/api/v2/property/dubai/buy/apartment-for-sale/?limit=50&page={page}")
        response = r.json()
        data: dict = response.get("data")
        return data.get("results") if data.get('next') else {}

    def get_fake_estate_duplex(self):
        r = req(method="GET",
                url="https://api.axcapital.ae/api/v2/property/dubai/buy/duplex-for-sale/?limit=10&page=1")
        response = r.json()
        data: dict = response.get("data")
        return data.get("results") if data.get('count') else {}

    def get_fake_estate_penthouse(self):
        r = req(method="GET",
                url=f"https://api.axcapital.ae/api/v2/property/dubai/buy/penthouse-for-sale/?limit=15&page=1")
        response = r.json()
        data: dict = response.get("data")
        return data.get("results") if data.get('count') else {}

    def get_fake_estate_villa(self):
        r = req(method="GET",
                url="https://api.axcapital.ae/api/v2/property/dubai/buy/villa-for-sale/?limit=45&page=1")
        response = r.json()
        data: dict = response.get("data")
        return data.get("results") if data.get('count') else {}

    def get_start_cities(self):
        with transaction.atomic():
            for city_data in CITIES:
                City.objects.get_or_create(**city_data)

    def get_start_estate_type(self):
        with transaction.atomic():
            for estate_type in ESTATE_TYPES:
                EstateType.objects.get_or_create(**estate_type)

    def random_date(self):
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2025, 12, 31)

        random_days = randint(0, (end_date - start_date).days)
        random_time = uniform(0, 1)
        random_datetime = start_date + timedelta(days=random_days, seconds=random_time * 24 * 60 * 60)

        return random_datetime.strftime('%Y-%m-%d')

    def get_start_data(self):
        if len(City.objects.all()) < 3 and len(EstateType.objects.all()) < 5:
            self.get_start_cities()
            self.get_start_estate_type()
        print('[FAKE NEWS]: Start data created')

    def get_cities(self) -> list[City]:
        return City.objects.all()

    def create_facilities(self, facility):
        obj, _ = Facilities.objects.get_or_create(type=facility.lower())
        return obj

    def create_project(self, project_data, facilities) -> Project:
        try:
            obj = Project.objects.get(name=project_data.get('name'))
            return obj
        except Project.DoesNotExist:
            obj = Project.objects.create(**project_data)
            obj.facilities.add(*facilities)
            obj.save()
            print(f'[FAKE NEWS]: Project `{project_data.get("name")}` created')
            return obj

    def create_estate_type(self, estate_type_data: str) -> EstateType:
        obj, _ = EstateType.objects.get_or_create(type_en=estate_type_data.lower())
        return obj

    def create_facilities(self, facility):
        obj, _ = Facilities.objects.get_or_create(type_en=facility.lower())
        return obj

    def save_image(self, estate: Estate, images: list):
        for image in images[:10]:
            img = image.get('image').get('jpeg')
            response = req(method='GET', url=img)
            if response.status_code == 200:
                estate_image = EstateImage(estate=estate)
                estate_image.img.save(img.split('/')[-1], File(BytesIO(response.content)))
                estate_image.save()

    def save_data(self, estate_data: dict):
        r = req(method='GET', url=f"https://www.axcapital.ae/buy/{estate_data.get('slug')}")
        loop_response = r.text
        tree = Selector(text=loop_response)
        description = tree.xpath('//p[@class="mb-11 whitespace-pre-line text-white60"]/text()').extract_first()
        facilities = tree.xpath('//div[@class="flex min-h-[65px] items-center whitespace-pre-wrap '
                                'border-b-[1px] border-r-[1px] border-borderMain px-6 text-lg text-white"]/span')

        project = {
            "name": estate_data.get('subcommunity'),
            "location": estate_data.get('location'),
            "developer": "null",
            "completion": self.random_date(),
            "is_furnished": estate_data.get('furnished'),
            "pdf_catalog": "catalog/fake_catalog.pdf"
        }
        facilities = [self.create_facilities(f.css('::text').get()) for f in facilities]

        p = self.create_project(project, facilities)

        estate_obj = {"title_en": estate_data.get("title"),
                      "project": p,
                      "area": round(estate_data.get("size") / 3.2808, 2),
                      "description_en": description,
                      "price_usd": round(estate_data.get("price") * 0.27),
                      "estate_type": self.create_estate_type(estate_data.get("property_type")),
                      "city": choice(self.cities),
                      "is_secondary": False,
                      "visits": randint(10, 100)}

        estate = Estate.objects.create(**estate_obj)
        images = estate_data.get('image_data')
        self.save_image(estate=estate, images=images)

        print(f'[FAKE NEWS]: Estate `{estate_data.get("title")}` created')
        return estate

    def post(self, request, *args, **kwargs):
        self.get_start_data()
        self.cities = self.get_cities()

        # villas = self.get_fake_estate_villa()
        # for villa in villas:
        #     self.save_data(villa)

        # duplexes = self.get_fake_estate_duplex()
        # for duplex in duplexes:
        #     self.save_data(duplex)

        penthouses = self.get_fake_estate_penthouse()
        for penthouse in penthouses:
            self.save_data(penthouse)
        #
        # for page in range(1, 11):
        #     apartments = self.get_fake_estate_apartment(page)
        #     for apartment in apartments:
        #         self.save_data(apartment)
        print("[FAKE NEWS]: All fake data created successfully")

        return self.create(request, *args, **kwargs)
