from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'id',
            'city_name',
            'city_description',
            'city_img',
        ]


class CityValidateSerializer(serializers.Serializer):
    city_name = serializers.CharField(max_length=20)
    city_name_ar = serializers.CharField(max_length=20)
    city_name_tr = serializers.CharField(max_length=20)
    city_name_ru = serializers.CharField(max_length=20)
    city_description = serializers.CharField(max_length=500)
    city_description_ar = serializers.CharField(max_length=500)
    city_description_tr = serializers.CharField(max_length=500)
    city_description_ru = serializers.CharField(max_length=500)

    class Meta:
        model = City

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
