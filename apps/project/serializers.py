from rest_framework import serializers

from .models import Project, Facilities


class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ['type',
                  'icon']


class ProjectSerializer(serializers.ModelSerializer):
    facilities = FacilitiesSerializer(many=True)
    completion = serializers.DateField(format='%m, %Y')

    class Meta:
        model = Project
        fields = [
            'name',
            'facilities',
            'location',
            'completion',
            'is_furnished',
            'pdf_catalog',
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'location',
        ]
