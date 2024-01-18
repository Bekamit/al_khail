import phonenumbers
from django.utils import timezone
from django.utils.translation import get_language_from_request
from rest_framework import serializers
from .models import Appeal

from apps.estate.models import Estate


class PhoneNumberField(serializers.CharField):
    def to_internal_value(self, data):
        try:
            parsed_number = phonenumbers.parse(data, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise serializers.ValidationError('Invalid phone number')
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError('Invalid phone number format')


class LanguageField(serializers.CharField):
    def to_representation(self, value):
        request = self.context.get('request')
        lang = get_language_from_request(request)
        return lang or super(LanguageField, self).to_representation(value)


class AppealBuyValidateSerializer(serializers.Serializer):
    estate_id = serializers.CharField()
    name = serializers.CharField(max_length=70, required=True)
    last_name = serializers.CharField(max_length=70, required=False)
    phone = PhoneNumberField()
    lang = LanguageField(max_length=30)
    at_time = serializers.DateTimeField(required=True)
    is_for_purchase = serializers.BooleanField(default=True)

    def validate_name(self, name):
        if any(char.isdigit() for char in name):
            raise serializers.ValidationError('Name should not contain numbers')
        if not name.isalpha():
            raise serializers.ValidationError('Name should not contain signs')
        return name

    def validate_last_name(self, last_name):
        if last_name:
            raise serializers.ValidationError('Last name must be empty')
        return last_name

    def validate_estate_id(self, estate_id):
        if not Estate.objects.filter(id=estate_id).exists():
            raise serializers.ValidationError('estate_id does not exist')
        return estate_id

    def validate_at_time(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("at_time must be in the future")
        return value

    def create(self, validated_data):
        last_name = validated_data.get('last_name', None)
        estate_id = validated_data['estate_id']

        try:
            estate_instance = Estate.objects.get(id=estate_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Estate с указанным id не существует')

        if last_name:
            raise serializers.ValidationError('Фамилия должна быть пустой')

        return Appeal.objects.create(
            is_for_purchase=validated_data['is_for_purchase'],
            estate_id=estate_instance,
            name=validated_data['name'],
            last_name=last_name,
            phone=validated_data['phone'],
            lang=validated_data['lang'],
            at_time=validated_data['at_time']
        )


class AppealSellValidateSerializer(serializers.Serializer):
    is_for_purchase = serializers.BooleanField(default=False)
    name = serializers.CharField(max_length=70, required=True)
    last_name = serializers.CharField(max_length=70, required=False)
    phone = PhoneNumberField()
    lang = LanguageField(max_length=30)
    at_time = serializers.DateTimeField(required=True)
    estate_id = serializers.PrimaryKeyRelatedField(queryset=Estate.objects.all(), required=False)

    def validate_name(self, name):
        if any(char.isdigit() for char in name):
            raise serializers.ValidationError('Name should not contain numbers')
        if not name.isalpha():
            raise serializers.ValidationError('Name should not contain signs')
        return name

    def validate_last_name(self, last_name):
        if last_name:
            raise serializers.ValidationError('Last name must be empty')
        return last_name

    def validate_at_time(self, time):
        if time <= timezone.now():
            raise serializers.ValidationError("at_time must be in the future")
        return time

    def create(self, validated_data):
        last_name = validated_data.get('last_name', None)

        if last_name:
            raise serializers.ValidationError('Last name must be empty')

        return Appeal.objects.create(
            is_for_purchase=validated_data['is_for_purchase'],
            name=validated_data['name'],
            last_name=last_name,
            phone=validated_data['phone'],
            lang=validated_data['lang'],
            at_time=validated_data['at_time']
        )
