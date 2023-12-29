from rest_framework import serializers
from .models import StaticData


class StaticDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticData
        fields = '__all__'
