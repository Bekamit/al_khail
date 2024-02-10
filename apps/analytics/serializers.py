import phonenumbers
from django.utils import timezone
from django.utils.translation import get_language_from_request
from rest_framework import serializers
from .models import CatalogDownloader, Appeal, Consultation
from apps.staticdata.models import Form
from .models import CatalogDownloader, Appeal
from apps.estate.models import Estate
from django.utils.translation import gettext_lazy as _
from apps.staticdata.serializers import CustomGetSerializer


class PhoneNumberField(serializers.CharField):
    def to_internal_value(self, data):
        try:
            parsed_number = phonenumbers.parse(data, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise serializers.ValidationError('Invalid phone number')
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError('Invalid phone number format')


class GetStaticDataSerializer(serializers.ModelSerializer):
    form = CustomGetSerializer()

    class Meta:
        model = Consultation
        fields = [
            'form',
        ]


class PostStaticDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'



class ChoiceRoleSerializer(serializers.ModelSerializer):
    placeholder = serializers.CharField(source='role')

    class Meta:
        model = Form
        fields = [
            'placeholder',
            'agent',
            'buyer',
            'exploring'
        ]


class CatalogDownloaderSerializer(PostStaticDataSerializer):
    class Meta(PostStaticDataSerializer.Meta):
        ...
class CatalogDownloaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogDownloader
        fields = ['name',
                  'phone',
                  'email',
                  'role']

    def create(self, validated_data):
        return CatalogDownloader.create_downloader(**validated_data)


class AppealSellValidateSerializer(PostStaticDataSerializer):
    is_for_purchase = serializers.BooleanField(default=False)
    name = serializers.CharField(max_length=70, required=True)
    last_name = serializers.CharField(max_length=70, required=True, allow_blank=True, write_only=True)
    phone = PhoneNumberField()
    at_time = serializers.DateField(required=True)
    city = serializers.CharField(max_length=70, required=True)

    def get_language(self):
        request = self.context['request']
        return get_language_from_request(request)

    def validate_last_name(self, last_name):
        if last_name:
            raise serializers.ValidationError(_('Wrong format'))
        return last_name

    def validate_at_time(self, time):
        if time <= timezone.now():
            raise serializers.ValidationError(_("at_time must be in the future"))
        return time

    def create(self, validated_data):
        validated_data.pop('last_name')
        validated_data['lang'] = self.get_language()
        validated_data['city'] = validated_data['city'].capitalize()
        return Appeal.create_appeal(validated_data)

    class Meta:
        model = Appeal
        fields = '__all__'


class AppealBuyValidateSerializer(PostStaticDataSerializer):
    is_for_purchase = serializers.BooleanField(default=True)
    estate_id = serializers.CharField()
    name = serializers.CharField(max_length=70, required=True)
    last_name = serializers.CharField(max_length=70, required=True, allow_blank=True, write_only=True)
    phone = PhoneNumberField()
    at_time = serializers.DateField(required=True)
    city = serializers.CharField(max_length=70, required=True)

    def validate_estate_id(self, estate_id):
        if not Estate.is_valid(estate_id):
            raise serializers.ValidationError(_('estate id does not exist'))
        return estate_id

    def get_language(self):
        request = self.context['request']
        return get_language_from_request(request)

    def validate_last_name(self, last_name):
        if last_name:
            raise serializers.ValidationError(_('Wrong format'))
        return last_name

    def validate_at_time(self, time):
        if time <= timezone.now():
            raise serializers.ValidationError(_("at_time must be in the future"))
        return time

    def create(self, validated_data):
        validated_data.pop('last_name')
        validated_data['lang'] = self.get_language()
        validated_data['city'] = validated_data['city'].capitalize()
        return Appeal.create_appeal(validated_data)


class ConsultationSerializer(PostStaticDataSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'
