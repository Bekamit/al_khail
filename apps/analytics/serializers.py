from rest_framework import serializers

from apps.analytics.models import DownloadCatalog
from apps.appeal.serializers import PhoneNumberField


class DownloadCatalogSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(required=False)

    class Meta:
        model = DownloadCatalog
        fields = '__all__'

    def create(self, validated_data):
        instance = DownloadCatalog.create_analytics(validated_data)
        return instance
