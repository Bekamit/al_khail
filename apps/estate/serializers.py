from rest_framework import serializers

from .models import Estate, EstateType
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
class BaseEstateSerializer(serializers.ModelSerializer):
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


class EstateRetrieveSerializer(BaseEstateSerializer):
    estate_type = serializers.StringRelatedField()
    project = ProjectSerializer()

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
                  'images',
                  'project', ]


class EstateSerializer(BaseEstateSerializer):
    project = ProjectListSerializer()

    class Meta:
        model = Estate
        fields = ['id',
                  'price_usd',
                  'city',
                  'project',
                  'images']
