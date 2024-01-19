from rest_framework import serializers, exceptions
from django.db import models

from .models import Estate, EstateType, EstateImage
from ..project.serializers import ProjectSerializer


# ------------------------ ESTATE IMAGE -------------------
class EstateImageListSerializer(serializers.Serializer):
    estate_id = serializers.SerializerMethodField()
    images = serializers.ListField(child=serializers.CharField())

    def get_estate_id(self, data):
        estate_id = data.get('estate_id')
        if not Estate.is_valid(estate_id):
            raise exceptions.ValidationError('estate id does not exist')
        return estate_id

    class Meta:
        model = EstateImage
        fields = ['estate_id',
                  'images']


# ------------------------ ESTATE TYPE -------------------


class EstateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateType
        fields = ['id',
                  'type']


# ------------------------- ESTATE -----------------------


class EstateRetrieveSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    estate_type = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = Estate
        fields = ['project',
                  'id',
                  'title',
                  'area',
                  'description',
                  'price_usd',
                  'estate_type',
                  'city',
                  'is_secondary']


class EstateSerializer(serializers.ModelSerializer):
    estate_type = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    preview = serializers.SerializerMethodField()

    def absolute_url(self, instance):
        if isinstance(instance.field, models.ImageField):
            return self.context['request'].build_absolute_uri(instance.url)
        return None

    def get_preview(self, estate):

        images = estate.image.all()
        preview_images = images.filter(img__icontains='preview')

        if preview_images.exists():
            return {'img': self.absolute_url(preview_images.first().img)}

        if images.exists():
            return {'img': self.absolute_url(images.first().img)}

        return {'img': self.absolute_url(estate.default_img)} if estate.default_img else None

    class Meta:
        model = Estate
        fields = ['id',
                  'title',
                  'area',
                  'description',
                  'price_usd',
                  'estate_type',
                  'city',
                  'is_secondary',
                  'preview']
