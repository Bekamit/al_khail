from drf_spectacular.utils import OpenApiParameter, extend_schema
from django.utils.translation import get_language_from_request
from rest_framework import status
from rest_framework.response import Response

from service.views import CustomSingletonListAPIView
from rest_framework.views import APIView

from .models import Header, Body, Form, Footer
from .serializers import HeaderSerializer, BodySerializer, FooterSerializer, FormSerializer


@extend_schema(
    summary="Получить все статичные данные",
    description="Класс представления AllStaticDataAPIView возвращает коллекцию всех статичных данных из моделей"
                " Header, Body, Form, Footer"
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["StaticData"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ]
)
class AllStaticDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        header = footer = Header.objects.first()
        body = Body.objects.first()
        form = Form.objects.first()
        header_serializer = HeaderSerializer(header)
        body_serializer = BodySerializer(body)
        form_serializer = FormSerializer(form)
        footer_serializer = FooterSerializer(footer)
        data = {
            "language": get_language_from_request(request).upper(),
            "static_data": {
                "header": header_serializer.data,
                "body": body_serializer.data,
                "forms": form_serializer.data,
                "footer": footer_serializer.data
            }
        }
        return Response(data, status=status.HTTP_200_OK)


@extend_schema(
    summary="Получить статичные данные HEADERa",
    description="Класс представления HeaderAPIView возвращает коллекцию всех статичных данных из Header "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["StaticData"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ]
)
class HeaderAPIView(CustomSingletonListAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
    response_key = "header"


@extend_schema(
    summary="Получить статичные данные BODY",
    description="Класс представления BodyAPIView возвращает коллекцию всех статичных данных из моделb Body "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["StaticData"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ]
)
class BodyAPIView(CustomSingletonListAPIView):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
    response_key = "body"


@extend_schema(
    summary="Получить статичные данные всех форм",
    description="Класс представления AllStaticDataAPIView возвращает коллекцию всех статичных данных из моделей Form "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["StaticData"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ]
)
class FormsAPIView(CustomSingletonListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    response_key = "forms"


@extend_schema(
    summary="Получить статичные данные FOOTERa",
    description="Класс представления AllStaticDataAPIView возвращает коллекцию всех статичных данных из моделей Footer "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["StaticData"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ]
)
class FooterAPIView(CustomSingletonListAPIView):
    queryset = Header.objects.all()
    serializer_class = FooterSerializer
    response_key = "footer"
