from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import Estate, EstateImage, EstateType
from .serializers import (EstateSerializer,
                          EstateValidateSerializer,
                          EstateImageValidateSerializer,
                          EstateImageSerializer,
                          EstateTypeValidateSerializer,
                          EstateTypeSerializer)


class EstateListAPIView(ListAPIView):
    queryset = Estate.objects.prefetch_related('image').all()
    serializer_class = EstateSerializer


class EstateCreateAPIView(CreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateValidateSerializer


class EstateRetrieveAPIView(RetrieveAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer
    lookup_field = 'id'


class EstateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    ...


class EstateTypeListAPIView(ListAPIView):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeSerializer


class EstateTypeCreateAPIView(CreateAPIView):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeValidateSerializer
