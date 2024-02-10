from drf_spectacular.utils import extend_schema
from .models import CatalogDownloader, Appeal, Consultation
from .serializers import CatalogDownloaderSerializer, AppealBuyValidateSerializer, AppealSellValidateSerializer, ConsultationSerializer
from rest_framework.generics import CreateAPIView
from .custom import CustomListCreateAPIView


@extend_schema(
    summary="Отправить запрос при скачивании каталога",
    description="Класс представления CatalogDownloaderCreateAPIView получает данные с формы при скачивании каталога проекта",
    methods=["POST"],
    tags=["Analytics"],
)
class CatalogDownloaderCreateAPIView(CustomListCreateAPIView):
    model = 'CatalogDownloader'
    queryset = CatalogDownloader.objects.all()
    serializer_class = CatalogDownloaderSerializer


@extend_schema(
    summary="Отправить запрос на покупку объекта недвижимости",
    description="Класс представления AppealBuyCreateAPIView получает данные с формы о покупке объекта недвижимости ",
    methods=["POST"],
    tags=["Analytics"],
)
class AppealBuyCreateAPIView(CustomListCreateAPIView):
    model = 'Appeal'
    queryset = Appeal.objects.all()
    serializer_class = AppealBuyValidateSerializer


@extend_schema(
    summary="Отправить запрос на продажу объекта недвижимости",
    description="Класс представления AppealSellCreateAPIView получает данные с формы о желании клиента"
                " продать свой объект недвижимости",
    methods=["POST"],
    tags=["Analytics"],
)
class AppealSellCreateAPIView(CustomListCreateAPIView):
    model = 'Appeal'
    queryset = Appeal.objects.all()
    serializer_class = AppealSellValidateSerializer


@extend_schema(
    summary="Отправить запрос на получения ответа своего вопроса",
    description="Класс представления ConsultationAPIView получает данные с формы о вопросе клиента",
    methods=["POST"],
    tags=["Analytics"],
)
class ConsultationCreateAPIView(CustomListCreateAPIView):
    model = 'Consultation'
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
