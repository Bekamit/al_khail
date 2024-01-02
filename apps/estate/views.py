from rest_framework.generics import ListAPIView, RetrieveAPIView
from service.views import CustomRetrieveImagesAPIView

from .models import Estate, EstateImage, EstateType
from .serializers import (EstateSerializer,
                          EstateRetrieveSerializer,
                          EstateTypeSerializer,
                          EstateImageListSerializer)


class EstateListAPIView(ListAPIView):
    queryset = Estate.objects.prefetch_related('image').all()
    serializer_class = EstateSerializer


class EstateRetrieveAPIView(RetrieveAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateRetrieveSerializer
    lookup_field = 'id'


class EstateTypeListAPIView(ListAPIView):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeSerializer


class EstateImageRetrieveAPIView(CustomRetrieveImagesAPIView):
    serializer_class = EstateImageListSerializer

    def get_queryset(self):
        estate_id = self.kwargs.get('id')
        queryset = EstateImage.objects.filter(estate_id=estate_id)
        return queryset
