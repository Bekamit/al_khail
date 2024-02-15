from drf_spectacular.utils import extend_schema, OpenApiParameter
from service.views import MultiSerializerListCreateAPIView
from service.cache import CustomCache

from .models import CatalogDownloader, Appeal
from apps.staticdata.models import Form

from .serializers import (CatalogDownloaderSerializer,
                          AppealBuyValidateSerializer,
                          AppealSellValidateSerializer,
                          ConsultationSerializer)
from apps.staticdata.serializers import (SellFormSerializer,
                                         SuccessFormSerializer,
                                         BuyFormSerializer,
                                         CatalogDownloaderFormSerializer,
                                         ConsultationFormSerializer)


@extend_schema(
    summary="Отправить запрос на консультацию/⏩cache_content",
    description="ConsultationMultiSerializerListCreateAPIView: \n\n "
                "При GET запросе отправляет поля формы на указаном языке;\n\n"
                "При POST запросе получает данные клиента и его вопросов с формы;\n\n"
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
class ConsultationMultiSerializerListCreateAPIView(MultiSerializerListCreateAPIView):
    method_get_queryset = Form.objects.all()
    method_post_queryset = Appeal.objects.all()
    method_get_serializer = ConsultationFormSerializer
    method_post_serializer = ConsultationSerializer
    response_serializer = SuccessFormSerializer
    response_key = 'form'
    cache_class = CustomCache
    cache_language = '__all__'
    cache_key = 'forms'


@extend_schema(
    summary="Отправить запрос на покупку объекта недвижимости/⏩cache_content",
    description="AppealBuyMultiSerializerListCreateAPIView: \n\n "
                "При GET запросе отправляет поля формы на указаном языке;\n\n"
                "При POST запросе получает данные с формы о желании клиента купить объект недвижимости;\n\n"
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
class AppealBuyMultiSerializerListCreateAPIView(MultiSerializerListCreateAPIView):
    method_get_queryset = Form.objects.all()
    method_post_queryset = Appeal.objects.all()
    method_get_serializer = BuyFormSerializer
    method_post_serializer = AppealBuyValidateSerializer
    response_serializer = SuccessFormSerializer
    response_key = 'form'
    cache_class = CustomCache
    cache_language = '__all__'
    cache_key = 'forms'


@extend_schema(
    summary="Отправить запрос на продажу объекта недвижимости/⏩cache_content",
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
    cache_class = CustomCache
    cache_language = '__all__'
    cache_key = 'forms'


@extend_schema(
    summary="Отправить запрос для аналитики скачивания каталога/⏩cache_content",
    description="CatalogDownloaderMultiSerializerListCreateAPIView: \n\n "
                "При GET запросе отправляет поля формы на указаном языке;\n\n"
                "При POST запросе получает данные с формы для аналитики скачивания каталога;\n\n"
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
class CatalogDownloaderMultiSerializerListCreateAPIView(MultiSerializerListCreateAPIView):
    method_get_queryset = Form.objects.all()
    method_post_queryset = CatalogDownloader.objects.all()
    method_get_serializer = CatalogDownloaderFormSerializer
    method_post_serializer = CatalogDownloaderSerializer
    response_serializer = SuccessFormSerializer
    response_key = 'form'
    cache_class = CustomCache
    cache_language = '__all__'
    cache_key = 'forms'
