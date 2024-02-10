from drf_spectacular.utils import extend_schema
from .models import CatalogDownloader, Appeal, Consultation
from .serializers import CatalogDownloaderSerializer, AppealBuyValidateSerializer, AppealSellValidateSerializer, ConsultationSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import CatalogDownloader, Appeal
from apps.staticdata.models import Form
from .serializers import CatalogDownloaderSerializer, AppealBuyValidateSerializer, AppealSellValidateSerializer
from apps.staticdata.serializers import SellFormSerializer, SuccessFormSerializer, BuyFormSerializer, CatalogDownloaderFormSerializer, ConsultationFormSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from service.views import MultiSerializerListCreateAPIView


@extend_schema(
    summary="Отправить запрос при скачивании каталога (в работе)",
    description="Класс представления CatalogDownloaderCreateAPIView получает данные с формы при скачивании каталога проекта",
    methods=["POST"],
    tags=["Analytics"],
)
class CatalogDownloaderCreateAPIView(CreateAPIView):
    model = 'CatalogDownloader'
    queryset = CatalogDownloader.objects.all()
    serializer_class = CatalogDownloaderSerializer


@extend_schema(
    summary="Отправить запрос на покупку объекта недвижимости(в работе)",
    description="Класс представления AppealBuyCreateAPIView получает данные с формы о покупке объекта недвижимости ",
    methods=["POST"],
    tags=["Analytics"],
)
class AppealBuyCreateAPIView(CreateAPIView):
    model = 'Appeal'
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
class AppealSellCreateAPIView(CreateAPIView):
    model = 'Appeal'
    queryset = Appeal.objects.all()
    serializer_class = AppealSellValidateSerializer


@extend_schema(
    summary="Отправить запрос на получения ответа своего вопроса",
    description="Класс представления ConsultationAPIView получает данные с формы о вопросе клиента",
    methods=["POST"],
    tags=["Analytics"],
)
class ConsultationCreateAPIView(CreateAPIView):
    model = 'Consultation'
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


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
    summary="Отправить запрос на покупку объекта недвижимости",
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


@extend_schema(
    summary="Отправить запрос для аналитики скачивания каталога",
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


@extend_schema(
    summary="Отправить запрос на консультацию",
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
    method_post_queryset = Form.objects.all()
    method_get_serializer = ConsultationFormSerializer
    method_post_serializer = ConsultationSerializer
    response_serializer = SuccessFormSerializer
    response_key = 'form'
