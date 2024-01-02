from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Estate, EstateType, EstateImage


# ------------------------- ESTATE IMAGES -----------------------
class EstateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateImage
        fields = ['img']


class EstateImageListSerializer(serializers.Serializer):
    estate_id = serializers.CharField()
    images = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = EstateImage
        fields = ['estate_id',
                  'images']


# ------------------------ ESTATE TYPE -------------------


class EstateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateType
        fields = ['type']


# ------------------------- ESTATE -----------------------


class EstateRetrieveSerializer(serializers.ModelSerializer):
    estate_type = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = Estate
        fields = ['id',
                  'name',
                  'developer',
                  'area',
                  'district',
                  'description',
                  'estate_type',
                  'city',
                  'is_secondary',
                  'create_at']


class EstateSerializer(EstateRetrieveSerializer):
    preview = serializers.SerializerMethodField()

    def get_preview(self, estate):
        images = estate.image
        try_preview = images.filter(img__icontains='preview')

        if images:
            if try_preview:
                ser = EstateImageSerializer(try_preview.first())
                return ser.data
            else:
                ser = EstateImageSerializer(images.first())
                return ser.data
        else:
            return None # написать выдачу дефолтного изображения, хранения дефолта скорее всего в StaticData

    class Meta:
        model = Estate
        fields = ['id',
                  'name',
                  'developer',
                  'area',
                  'district',
                  'description',
                  'estate_type',
                  'city',
                  'is_secondary',
                  'preview']
