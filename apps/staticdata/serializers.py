from rest_framework import serializers
from .models import Header, Body, Form, DefaultValue


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['buy',
                  'all_properties',
                  'place_ad',
                  'contact_as',
                  'slogan',
                  'search',
                  'city',
                  'estate_type',
                  'show_result',
                  'filter',
                  'all',
                  'popular',
                  'new_add']


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ['property',
                  'about_company',
                  'why',
                  'advantages',
                  'all_properties',
                  'view_more',
                  'listing_details',
                  'facilities',
                  'download_catalog',
                  'description',
                  'you_might_like', ]


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['buy',
                  'all_properties',
                  'place_ad',
                  'contact_as']


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['callback_form_title',
                  'sell_form_title',
                  'download_catalog_form_title',
                  'form_description',
                  'your_name',
                  'your_email',
                  'your_phone',
                  'your_city',
                  'at_date',
                  'send',
                  'role',
                  'agent',
                  'buyer',
                  'exploring',
                  'download', ]


