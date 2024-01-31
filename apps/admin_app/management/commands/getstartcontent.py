from io import BytesIO

from django.core.files.base import File
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.staticdata.start_content import CITIES, ESTATE_TYPES, COMPANY, DEFAULT_VALUES, FACILITIES

from apps.estate.models import EstateType
from apps.city.models import City
from apps.company.models import Company
from apps.project.models import Facilities
from apps.staticdata.models import Header, Body, Form, Footer, DefaultValue


class Command(BaseCommand):
    help = 'Add static content on all languages(en, ar, tr, ru) in database'
    city = City.objects.all()
    estate_type = EstateType.objects.all()
    default_value = DefaultValue.objects.all()
    company = Company.objects.all()
    facilities = Facilities.objects.all()

    def add_arguments(self, parser):
        parser.add_argument('-a', '--all', action='store_true', help='Add all start content')
        parser.add_argument('-ct', '--city', action='store_true', help='Add start cities')
        parser.add_argument('-c', '--company', action='store_true', help='Add start about company')
        parser.add_argument('-s', '--static_content', action='store_true', help='Add static content')
        parser.add_argument('-t', '--estate_type', action='store_true', help='Add start estate types')
        parser.add_argument('-f', '--facilities', action='store_true', help='Add start facilities')
        parser.add_argument('-d', '--default_value', action='store_true', help='Add default value')

    def get_start_cities(self):
        with transaction.atomic():
            for city_data in CITIES:
                img_path = city_data.pop("city_img")
                city, _ = City.objects.get_or_create(**city_data)
                with open(img_path, 'rb') as image_file:
                    image = image_file.read()
                    city.city_img.save(img_path.split('/')[-1], File(BytesIO(image)))
                    city.save()
        self.stdout.write(self.style.SUCCESS('Cities created successfully'))

    def get_start_estate_type(self):
        with transaction.atomic():
            for estate_type in ESTATE_TYPES:
                EstateType.objects.get_or_create(**estate_type)
        self.stdout.write(self.style.SUCCESS('Estate Types created successfully'))

    def get_start_facilities(self):
        with transaction.atomic():
            for facilities_data in FACILITIES:
                Facilities.objects.get_or_create(**facilities_data)
        self.stdout.write(self.style.SUCCESS('Facilities created successfully'))

    def get_default_image(self):
        img_path = DEFAULT_VALUES.get("default_image")
        with open(img_path, 'rb') as image_file:
            image = image_file.read()
            default = DefaultValue.objects.create()
            default.default_image.save(img_path.split('/')[-1], File(BytesIO(image)))
            default.save()
        self.stdout.write(self.style.SUCCESS('Default image created successfully'))

    def get_about_company(self):
        with transaction.atomic():
            logo_path = COMPANY.pop("company_img")
            company, _ = Company.objects.get_or_create(**COMPANY)
            with open(logo_path, 'rb') as image_file:
                image = image_file.read()
                company.company_img.save(logo_path.split('/')[-1], File(BytesIO(image)))
                company.save()
            self.stdout.write(self.style.SUCCESS('About company created successfully'))

    def get_start_data(self):
        if not self.company:
            self.get_about_company()
        if not self.default_value:
            self.get_default_image()
        if self.city.count() < 3:
            self.get_start_cities()
        if self.estate_type.count() < 5:
            self.get_start_estate_type()
        if not self.facilities:
            self.get_start_facilities()

    def handle(self, *args, **options):
        if options['all']:
            try:
                self.get_start_data()
                self.stdout.write(self.style.SUCCESS('--Static content created successfully--'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Static content error: {e}'))
        else:
            if options['city']:
                self.get_start_cities()
            if options['company']:
                self.get_about_company()
            if options['static_content']:
                self.stdout.write(self.style.ERROR(f'Not yet this function!'))
            if options['estate_type']:
                self.get_start_estate_type()
            if options['facilities']:
                self.get_start_facilities()
            if options['default_value']:
                self.get_default_image()
