from rest_framework import serializers
from .models import CatalogDownloader
from apps.staticdata.models import Form


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


class CatalogDownloaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogDownloader
        fields = ['name',
                  'phone',
                  'email',
                  'role']
