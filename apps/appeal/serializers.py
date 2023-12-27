from rest_framework import serializers
from .models import Appeal
from django.utils import timezone


class AppealBuyValidateSerializer(serializers.Serializer):
    estate_id = serializers.PrimaryKeyRelatedField(queryset=Appeal.objects.all())
    name = serializers.CharField(max_length=70, required=True)
    last_name = serializers.CharField(max_length=70)
    phone = serializers.CharField(max_length=70, required=True)
    lang = serializers.CharField(max_length=30, required=True)
    at_time = serializers.DateTimeField(required=True)
    is_for_purchase = serializers.BooleanField(default=False)

    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError('Name should not contain numbers')
        return value

    def validate_phone(self, value):
        if not value.startswith('+'):
            raise serializers.ValidationError('Phone number should start with \'+\'')
        return value

    def validate_at_time(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("at_time must be in the future")
        return value

    def create(self, validated_data):
        return Appeal.objects.create(
            is_for_purchase=validated_data['is_for_purchase'],
            estate_id=validated_data['estate_id'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            lang=validated_data['lang'],
            at_time=validated_data['at_time']
        )


class AppealSellValidateSerializer(serializers.Serializer):
    is_for_purchase = serializers.BooleanField(default=False)
    name = serializers.CharField(max_length=70, required=True)
    phone = serializers.CharField(max_length=70, required=True)
    lang = serializers.CharField(max_length=30, required=True)
    at_time = serializers.DateTimeField(required=True)
    estate_id = serializers.PrimaryKeyRelatedField(queryset=Appeal.objects.all(), required=False)

    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError('Name should not contain numbers')
        return value

    def validate_phone(self, value):
        if not value.startswith('+'):
            raise serializers.ValidationError('Phone number should start with \'+\'')
        return value

    def validate_at_time(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("at_time must be in the future")
        return value

    def create(self, validated_data):
        return Appeal.objects.create(
            is_for_purchase=validated_data['is_for_purchase'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            lang=validated_data['lang'],
            at_time=validated_data['at_time']
        )