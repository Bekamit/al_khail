from rest_framework import serializers

from .models import Appeal
from apps.estate.models import Estate
from django.utils import timezone


class AppealBuyValidateSerializer(serializers.Serializer):
    estate_id = serializers.PrimaryKeyRelatedField(queryset=Estate.objects.all())
    first_name = serializers.CharField(max_length=70, required=True)
    last_name = serializers.CharField(max_length=70, required=True)
    phone = serializers.CharField(max_length=70, required=True)
    lang = serializers.CharField(max_length=30)
    at_time = serializers.DateTimeField(required=False)
    is_for_purchase = serializers.BooleanField(default=True)

    def validate_first_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError('Name should not contain numbers')
        return value

    def validate_phone(self, value):
        if not value.startswith('+'):
            raise serializers.ValidationError('Phone number should start with \'+\'')
        return value

    def validate_at_time(self, value):
        # if value <= timezone.now():
        #     raise serializers.ValidationError("at_time must be in the future")
        return value

    def create(self, validated_data):
        return Appeal.objects.create(
            is_for_purchase=validated_data['is_for_purchase'],
            estate_id=validated_data['estate_id'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            lang=validated_data['lang'],
        )


class AppealSellValidateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=70, required=True)
    last_name = serializers.CharField(max_length=70, required=True)
    phone = serializers.CharField(max_length=70, required=True)
    lang = serializers.CharField(max_length=30, required=True)
    at_time = serializers.DateTimeField(required=False)
    is_for_purchase = serializers.BooleanField(default=False)

    def validate_first_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError('Name should not contain numbers')
        return value

    def validate_phone(self, value):
        if not value.startswith('+'):
            raise serializers.ValidationError('Phone number should start with \'+\'')
        return value

    def validate_at_time(self, value):
        # if value <= timezone.now():
        #     raise serializers.ValidationError("at_time must be in the future")
        return value

    def create(self, validated_data):
        instance = Appeal.objects.create(**validated_data)
        return instance
