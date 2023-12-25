from rest_framework import serializers
from .models import Appeal, AppealType


class AppealTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppealType
        fields = '__all__'


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'
