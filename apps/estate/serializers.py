from rest_framework import serializers, exceptions
from django.db import models
from django.utils.translation import gettext_lazy as _

from .models import Estate, EstateType, EstateImage
from apps.staticdata.models import DefaultValue
from apps.project.serializers import ProjectSerializer, ProjectListSerializer


# ------------------------ ESTATE IMAGE -------------------
class EstateImageListSerializer(serializers.Serializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Estate
        fields = ['id',
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
        fields = ['id',
                  'title',
                  'area',
                  'description',
                  'price_usd',
                  'estate_type',
                  'city',
                  'is_secondary',
                  'project', ]


class EstateSerializer(serializers.ModelSerializer):
    project = ProjectListSerializer()
    # estate_type = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    images = serializers.StringRelatedField(many=True)

    def absolute_url(self, path):
        return self.context['request'].build_absolute_uri(path)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if images := representation.get('images'):
            representation['images'] = [self.absolute_url(image) for image in images]
        else:
            default_img = DefaultValue.default_img()
            representation['images'] = self.absolute_url(default_img.url) if default_img else []
        return representation

    # preview = serializers.SerializerMethodField()

    # def absolute_url(self, instance):
    #     if isinstance(instance.field, models.ImageField):
    #         return self.context['request'].build_absolute_uri(instance.url)
    #     return instance.url

    # def get_preview(self, estate):
    #     if image := estate.image.first():
    #         return {'img': self.absolute_url(image.img)}
    #     else:
    #         return {'img': self.absolute_url(DefaultValue.default_img())}

    class Meta:
        model = Estate
        fields = ['id',
                  'price_usd',
                  'city',
                  'project',
                  'images']
