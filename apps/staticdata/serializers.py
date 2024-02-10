from rest_framework import serializers
from .models import Header, Body, Form, Footer, Error404
from ..analytics.models import Consultation


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = [
            'city',
            'all_real_estates',
            'place_ad',
            'about_us', ]


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = [
            'main',
            'search',
            'slogan',
            'see_real_estates',
            'city',
            'estate_type',
            'popular',
            'new_add',
            'all',
            'show_result',
            'we_have',
            'benefits',
            'wide_selection',
            'wide_selection_description',
            'confidentiality',
            'confidentiality_description',
            'exclusive_offers',
            'exclusive_offers_description',
            'feedback',
            'feedback_description',
            'furnished',
            'completion',
            'price_at',
            'catalog',
            'features_and_amenities',
            'description',
            'similar_properties',
            'mission_and_history',
            'mission',
            'history',
            'company',
        ]


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = [
            'contact_us',
            'cities',
            'estate_types',
            'pages'
        ]


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'contact_us',
            'any_question',
            'leave_your_contacts',
            'submit_application',
            'fill_form',
            'sell_with_us',
            'successfully',
            'thanks',
            'download_catalog',
            'your_name',
            'your_email',
            'phone_number',
            'your_city',
            'date',
            'send',
            'close',
            'download',
            'select_role',
            'agent',
            'buyer',
            'exploring',

        ]


class CustomGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'your_name',
            'your_phone',
            'your_city',
            'at_date',
        ]


class CustomPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'


class Error404Serializer(serializers.ModelSerializer):
    class Meta:
        model = Error404
        fields = [
            'not_found',
            'error_description',
        ]


class SuccessFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'successfully',
            'thanks',
            'close',
        ]


class SellFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'sell_with_us',
            'fill_form',
            'your_name',
            'phone_number',
            'your_city',
            'date',
            'send',
        ]


class BuyFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'submit_application',
            'fill_form',
            'your_name',
            'phone_number',
            'your_city',
            'date',
            'send',
        ]


class CatalogDownloaderFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'submit_application',
            'fill_form',
            'your_name',
            'your_email',
            'phone_number',
            'select_role',
            'your_city',
        ]


class ConsultationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'submit_application',
            'fill_form',
            'your_name',
            'phone_number',
            'your_city',
            'date',
        ]
