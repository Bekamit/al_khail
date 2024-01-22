from rest_framework.generics import CreateAPIView
from .models import DownloadCatalog
from .serializers import DownloadCatalogSerializer


class DownloadCatalogAPIView(CreateAPIView):
    queryset = DownloadCatalog.objects.all()
    serializer_class = DownloadCatalogSerializer
