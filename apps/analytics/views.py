from .models import DownloadCatalog
from .serializers import DownloadCatalogSerializer
from drf_spectacular.utils import extend_schema
from .models import CatalogDownloader, Appeal
from .serializers import CatalogDownloaderSerializer, AppealBuyValidateSerializer, AppealSellValidateSerializer
from rest_framework.generics import CreateAPIView


class DownloadCatalogAPIView(CreateAPIView):
    queryset = DownloadCatalog.objects.all()
    serializer_class = DownloadCatalogSerializer


@extend_schema(
    summary="Отправить запрос при скачивании каталога",
    description="Класс представления CatalogDownloaderCreateAPIView получает данные с формы при скачивании каталога проекта",
    methods=["POST"],
    tags=["Analytics"],
)
class CatalogDownloaderCreateAPIView(CreateAPIView):
    queryset = CatalogDownloader.objects.all()
    serializer_class = CatalogDownloaderSerializer


@extend_schema(
    summary="Отправить запрос на покупку объекта недвижимости",
    description="Класс представления AppealBuyCreateAPIView получает данные с формы о покупке объекта недвижимости ",
    methods=["POST"],
    tags=["Analytics"],
)
class AppealBuyCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealBuyValidateSerializer


@extend_schema(
    summary="Отправить запрос на продажу объекта недвижимости",
    description="Класс представления AppealSellCreateAPIView получает данные с формы о желании клиента"
                " продать свой объект недвижимости",
    methods=["POST"],
    tags=["Analytics"],
)
class AppealSellCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSellValidateSerializer
