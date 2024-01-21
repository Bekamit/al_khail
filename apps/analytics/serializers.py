from rest_framework import serializers

from apps.analytics.models import Analytics, Role
from apps.appeal.serializers import PhoneNumberField


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class AnalyticsSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()
    message = serializers.CharField(allow_blank=True, required=False, allow_null=True)

    class Meta:
        model = Analytics
        fields = '__all__'
