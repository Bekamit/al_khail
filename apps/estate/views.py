from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import RetrieveAPIView

from service.views import CustomRetrieveImagesAPIView, CustomListAPIView

from .models import Estate, EstateImage, EstateType
from .serializers import (EstateSerializer,
                          EstateRetrieveSerializer,
                          EstateTypeSerializer,
                          EstateImageListSerializer)


@extend_schema(
    summary="Получить список типов недвижимости",
    description="Класс представления EstateTypeListAPIView возвращает коллекцию из всех типов недвижимости модели "
                "EstateType "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["EstateType"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (опционально).'
        ),
    ],
)
class EstateTypeListAPIView(CustomListAPIView):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeSerializer
    response_key = 'estate types'


@extend_schema(
    summary="Получить список объектов недвижимости",
    description="Класс представления EstateListAPIView возвращает коллекцию из всех объектов недвижимости модели Estate "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["Estate"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (опционально).'
        ),
    ],
)
class EstateListAPIView(CustomListAPIView):
    queryset = Estate.objects.prefetch_related('image').all()
    serializer_class = EstateSerializer
    response_key = 'estates'


@extend_schema(
    summary="Получить объект недвижимости по id",
    description="Класс представления EstateRetrieveAPIView возвращает один объект недвижимости модели Estate "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["Estate"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (опционально).'
        ),
    ],
)
class EstateRetrieveAPIView(RetrieveAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateRetrieveSerializer
    lookup_field = 'id'


@extend_schema(
    summary="Получить коллекцию изображений недвижимости по id",
    description="Класс представления class EstateImageRetrieveAPIView возвращает коллекцию изображений для одного"
                " объекта недвижимости модели Estate",
    methods=["GET"],
    tags=["Estate"],
)
class EstateImageRetrieveAPIView(CustomRetrieveImagesAPIView):
    serializer_class = EstateImageListSerializer

    def get_queryset(self):
        estate_id = self.kwargs.get('id')
        queryset = EstateImage.objects.filter(estate_id=estate_id)
        return queryset
