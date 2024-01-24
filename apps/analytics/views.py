from .models import CatalogDownloader
from .serializers import CatalogDownloaderSerializer
from rest_framework.generics import ListCreateAPIView


class CatalogDownloaderCreateAPIView(ListCreateAPIView):
    queryset = CatalogDownloader.objects.all()
    serializer_class = CatalogDownloaderSerializer
