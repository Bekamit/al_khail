from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name',
                  'mission',
                  'history',
                  'company',
                  'phone',
                  'email',
                  'company_img',]
