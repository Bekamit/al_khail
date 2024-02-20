import phonenumbers
from django.utils import timezone
from django.utils.translation import get_language_from_request
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from apps.staticdata.models import Form
from .models import CatalogDownloader, Appeal
from apps.estate.models import Estate
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
import phonenumbers
from .models import CatalogDownloader, Appeal
from apps.estate.models import Estate
from django.core.validators import validate_email


class PhoneNumberField(serializers.CharField):
    def to_internal_value(self, data):
        try:
            parsed_number = phonenumbers.parse(data, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise serializers.ValidationError(_('Invalid phone number'))
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError(_('Invalid phone number format'))


class BaseAppealSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70, required=True)
    last_name = serializers.CharField(max_length=70, required=True, allow_blank=True, write_only=True)
    phone = PhoneNumberField(required=True)
    city = serializers.CharField(max_length=70, required=True)
    date = serializers.DateField(required=True)

    def get_language(self):
        request = self.context['request']
        return get_language_from_request(request)

    def validate_last_name(self, last_name):
        if last_name:
            raise serializers.ValidationError(_('Wrong format'))
        return last_name

    def validate_at_date(self, date):
        today = timezone.now().date()
        if date == today - timezone.timedelta(days=1):
            raise ValidationError(_('You can choice only future'))

    def reformat(self, validated_data):
        validated_data.pop('last_name')
        validated_data['lang'] = self.get_language()
        validated_data['city'] = validated_data['city'].capitalize()

    def create(self, validated_data):
        self.reformat(validated_data)
        return Appeal.create_appeal(validated_data)


class AppealSellValidateSerializer(BaseAppealSerializer):
    appeal_type = serializers.CharField(max_length=20, default='sell')

    class Meta:
        model = Appeal
        fields = '__all__'


class AppealBuyValidateSerializer(BaseAppealSerializer):
    appeal_type = serializers.CharField(max_length=20, default='buy')
    estate_id = serializers.CharField(required=True)

    def validate_estate_id(self, estate_id):
        if not Estate.is_valid(estate_id):
            raise serializers.ValidationError(_('estate id does not exist'))
        return estate_id

    def reformat(self, validated_data):
        validated_data.pop('last_name')
        validated_data['lang'] = self.get_language()

    def create(self, validated_data):
        self.reformat(validated_data)
        return Appeal.create_appeal(validated_data)


class ConsultationSerializer(BaseAppealSerializer):
    appeal_type = serializers.CharField(max_length=20, default='consultation')


class CatalogDownloaderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True)
    phone = PhoneNumberField(required=True)
    email = serializers.EmailField(required=True)
    role = serializers.CharField(max_length=30, required=True)
    estate_id = serializers.CharField()

    def get_language(self):
        request = self.context['request']
        return get_language_from_request(request)

    def validate_estate_id(self, estate_id):
        if not Estate.is_valid(estate_id):
            raise serializers.ValidationError(_('Estate id does not exist'))
        return estate_id

    def reformat(self, validated_data):
        validated_data['lang'] = self.get_language()

    def create(self, validated_data):
        self.reformat(validated_data)
        return CatalogDownloader.create_downloader(validated_data)
