from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Estate, EstateType, EstateImage


# ------------------------- ESTATE IMAGES -----------------------
class EstateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateImage
        fields = ['img']


class EstateImageValidateSerializer(serializers.Serializer):
    estate_id = serializers.IntegerField(min_value=1, required=True)
    img = serializers.ListField(child=serializers.ImageField())

    class Meta:
        model = EstateImage

    def validate_estate_id(self, estate_id):
        try:
            Estate.objects.get(id=estate_id)
        except Estate.DoesNotExist:
            raise ValidationError(f'estate_{estate_id} Does Not Exist')
        return estate_id

    def validate_img(self, list_field):
        if len(list_field) > 10: raise ValidationError(f'Max 10 images for one RealEstateObject')
        for image in list_field:
            if not image.name.split('.')[-1].lower() in ['jpg', 'jpeg', 'png']:
                raise ValidationError(f'Image: {image.name} have wrong format. Only `.JPG`, `.jpeg` & `.PNG`')
        return list_field

    def create(self, validated_data):
        images = validated_data.pop('img')
        data = []
        for image in images:
            obj = self.Meta.model.objects.create(estate_id=validated_data.get("estate_id"), img=image)
            data.append(obj.img)
        response_images = {"estate_id": validated_data.get('estate_id'),
                           "img": data}

        return response_images


# ------------------------ ESTATE TYPE -------------------


class EstateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateType
        fields = ['type']


class EstateTypeValidateSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=30, required=True)
    type_ar = serializers.CharField(max_length=30, required=True)
    type_tr = serializers.CharField(max_length=30, required=True)
    type_ru = serializers.CharField(max_length=30, required=True)

    class Meta:
        model = EstateType

    def validate_type(self, estate_type):
        if self.Meta.model.in_collection(estate_type=estate_type):
            raise ValidationError(f'{estate_type} already exist')
        return estate_type

    def validate_type_ar(self, estate_type):
        if self.Meta.model.in_collection(estate_type=estate_type):
            raise ValidationError(f'{estate_type} already exist')
        return estate_type

    def validate_type_tr(self, estate_type):
        if self.Meta.model.in_collection(estate_type=estate_type):
            raise ValidationError(f'{estate_type} already exist')
        return estate_type

    def validate_type_ru(self, estate_type):
        if self.Meta.model.in_collection(estate_type=estate_type):
            raise ValidationError(f'{estate_type} already exist')
        return estate_type

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)


# ------------------------- ESTATE -----------------------

class EstateSerializer(serializers.ModelSerializer):
    estate_type = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
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
            return None

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
                  'preview',
                  'create_at']


class EstateValidateSerializer(serializers.Serializer):
    """
    Multilanguage ModelValidateSerializer:
    model: Estate
    language: [(default: 'en'), 'ar', 'tr', 'ru']
    """
    name = serializers.CharField(max_length=100, required=True)
    name_ar = serializers.CharField(max_length=100, required=False)
    name_tr = serializers.CharField(max_length=100, required=False)
    name_ru = serializers.CharField(max_length=100, required=False)
    developer = serializers.CharField(max_length=100, required=True)
    developer_ar = serializers.CharField(max_length=100, required=False)
    developer_tr = serializers.CharField(max_length=100, required=False)
    developer_ru = serializers.CharField(max_length=100, required=False)
    area = serializers.FloatField(min_value=1.0)
    district = serializers.CharField(max_length=30, required=True)
    district_ar = serializers.CharField(max_length=30, required=False)
    district_tr = serializers.CharField(max_length=30, required=False)
    district_ru = serializers.CharField(max_length=30, required=False)
    description = serializers.CharField(max_length=1000, required=True)
    description_ar = serializers.CharField(max_length=1000, required=False)
    description_tr = serializers.CharField(max_length=1000, required=False)
    description_ru = serializers.CharField(max_length=1000, required=False)
    city_id = serializers.IntegerField(min_value=1, required=True)
    estate_type_id = serializers.IntegerField(min_value=1, required=True)
    is_secondary = serializers.BooleanField(default=True)

    class Meta:
        model = Estate

    def get_local_fields(self):
        fields = self.Meta.model._meta.get_fields()
        ar, tr, ru = [], [], []
        for field in fields:
            if field.name.endswith('ar'):
                ar.append(field.name)
            elif field.name.endswith('tr'):
                tr.append(field.name)
            elif field.name.endswith('ru'):
                ru.append(field.name)
        return ar, tr, ru

    def validate(self, data):
        local_groups = self.get_local_fields()
        for group in local_groups:

            all_empty = all(not data.get(field) for field in group)
            all_filled = all(data.get(field) for field in group)
            if not (all_empty or all_filled):
                raise ValidationError(
                    f"All fields for language group {group} must be either filled or empty.")
        return data

    def validate_city_id(self, city_id):
        if not self.Meta.model.city_id_is_valid(city_id=city_id):
            raise ValidationError(f'city_id: {city_id} does not exist')
        return city_id

    def validate_estate_type_id(self, estate_type_id):
        if not self.Meta.model.estate_type_id_is_valid(estate_type_id=estate_type_id):
            raise ValidationError(f'estate_type: {estate_type_id} does not exist')
        return estate_type_id

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
