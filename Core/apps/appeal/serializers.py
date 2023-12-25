from rest_framework import serializers
from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'


class AppealValidateSerializer(serializers.Serializer):
    ...
#     Добавить проеврку валидности данных с форм
