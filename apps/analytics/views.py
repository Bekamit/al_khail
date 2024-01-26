from .models import CatalogDownloader
from .serializers import CatalogDownloaderSerializer
from rest_framework.generics import CreateAPIView


class CatalogDownloaderCreateAPIView(CreateAPIView):
    queryset = CatalogDownloader.objects.all()
    serializer_class = CatalogDownloaderSerializer
