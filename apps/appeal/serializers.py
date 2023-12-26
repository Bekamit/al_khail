from rest_framework import serializers
from .models import Appeal
from django.utils import timezone



class AppealBuyValidateSerializer(serializers.Serializer):
    is_for_purchase = serializers.BooleanField(default=True)
    estate_id = serializers.PrimaryKeyRelatedField(queryset=Appeal.objects.all())
    name = serializers.CharField(max_length=70)
    phone = serializers.CharField(max_length=70)
    lang = serializers.CharField(max_length=30)
    at_time = serializers.DateTimeField()

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



class AppealSellValidateSerializer(serializers.Serializer):
    is_for_purchase = serializers.BooleanField(default=True)
    estate_id = serializers.PrimaryKeyRelatedField(queryset=Appeal.objects.all())
    name = serializers.CharField(max_length=70)
    phone = serializers.CharField(max_length=70)
    lang = serializers.CharField(max_length=30)
    at_time = serializers.DateTimeField()

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
