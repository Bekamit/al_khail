from rest_framework import status
from rest_framework.response import Response
from .models import CatalogDownloader, Consultation
from .serializers import CatalogDownloaderSerializer, ConsultationSerializer, GetStaticDataSerializer
from service.views import CustomListAPIView
from rest_framework.generics import CreateAPIView
from .serializers import GetStaticDataSerializer,PostStaticDataSerializer


class CustomListCreateAPIView(CustomListAPIView, CreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetStaticDataSerializer
        elif self.request.method == 'POST':
            return PostStaticDataSerializer
        else:
            return None

    def get(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class()

        if serializer_class == GetStaticDataSerializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)