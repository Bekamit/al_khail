from rest_framework import serializers

from apps.project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    facilities = serializers.StringRelatedField(many=True, read_only=True)
    completion = serializers.DateField(format='%m, %Y')

    class Meta:
        model = Project
        fields = [
            'name',
            'facilities',
            'location',
            'developer',
            'completion',
            'is_furnished',
            'pdf_catalog',
        ]
