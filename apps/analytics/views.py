from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import CatalogDownloader, Appeal
from apps.staticdata.models import Form
from .serializers import AppealBuyValidateSerializer, AppealSellValidateSerializer
from apps.staticdata.serializers import (SellFormSerializer,
                                         SuccessFormSerializer,
                                         CatalogDownloaderFormSerializer)
from rest_framework.generics import CreateAPIView
from service.views import MultiSerializerListCreateAPIView


@extend_schema(
    summary="Отправить запрос на покупку объекта недвижимости(в работе)",
    description="Класс представления AppealBuyCreateAPIView получает данные с формы о покупке объекта недвижимости ",
    methods=["POST"],
    tags=["Analytics"],
)
class AppealBuyCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealBuyValidateSerializer


@extend_schema(
    summary="Отправить запрос на продажу объекта недвижимости",
    description="AppealSellMultiSerializerListCreateAPIView: \n\n "
                "При GET запросе отправляет поля формы на указаном языке;\n\n"
                "При POST запросе получает данные с формы о желании клиента продать свой объект недвижимости;\n\n"
                "При ошибках возвращает ошибки по полям на нужном языке; при успешной отработке формы возвращает "
                "поля формы об успешной отработке формы и статус 201",
    methods=["GET",
             "POST"],
    tags=["Analytics"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ],
)
class AppealSellMultiSerializerListCreateAPIView(MultiSerializerListCreateAPIView):
    method_get_queryset = Form.objects.all()
    method_post_queryset = Appeal.objects.all()
    method_get_serializer = SellFormSerializer
    method_post_serializer = AppealSellValidateSerializer
    response_serializer = SuccessFormSerializer
    response_key = 'form'


@extend_schema(
    summary="Отправить запрос при скачивании каталога",
    description="Класс представления CatalogDownloaderMultiSerializerListCreateAPIView получает данные с формы при скачивании каталога проекта",
    methods=["GET",
             "POST"],
    tags=["Analytics"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ],
)
class CatalogDownloaderMultiSerializerListCreateAPIView(MultiSerializerListCreateAPIView):
    method_get_queryset = Form.objects.all()
    method_post_queryset = CatalogDownloader.objects.all()
    method_get_serializer = CatalogDownloaderFormSerializer
    method_post_serializer = AppealSellValidateSerializer
    response_serializer = SuccessFormSerializer
    response_key = 'form'
