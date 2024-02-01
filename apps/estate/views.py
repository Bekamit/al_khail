from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from service.views import (CustomRetrieveImagesAPIView,
                           CustomListAPIView,
                           CustomEstateCreateAPIView,
                           CustomRetrieveAPIView)

from .filters import EstateFilterSet
from .models import Estate, EstateImage, EstateType
from service.pagination import LimitOffsetCustomPagination
from .serializers import (EstateSerializer,
                          EstateRetrieveSerializer,
                          EstateTypeSerializer)


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
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
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
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
        OpenApiParameter(
            name='city_id',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Фильтр по городу'
        ),
        OpenApiParameter(
            name='estate_type_id',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Фильтр по типу недвижимости'
        ),
        OpenApiParameter(
            name='is_secondary',
            type=bool,
            location=OpenApiParameter.QUERY,
            description='Фильтр первичное/вторичное (true=вторичное)\n\n'
                        'Wikipedia: Жилье, которое уже сдано в эксплуатацию и на которое есть оформленное свидетельство'
                        ' о регистрации права собственности, называется вторичным. Под первичным же подразумевается '
                        'такое жилье, на которое еще нет права собственности или которое еще находится на стадии строительства.'
        ),
        OpenApiParameter(
            name='search',
            type=str,
            location=OpenApiParameter.QUERY,
            description='Поиск по location, developer & project.name на английском языке только!'
        ),
        OpenApiParameter(
            name='limit',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Количество результатов, возвращаемых на страницу \n\n'
                        'Example: http://127.0.0.1:8000/api/v1/estate/?limit=10&offset=21'
        ),
        OpenApiParameter(
            name='offset',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Начальный индекс, от которого идет отсчет.\n\n'
                        'Example: http://127.0.0.1:8000/api/v1/estate/?limit=10&offset=21'
        ),
        OpenApiParameter(
            name='project_id',
            type=int,
            location=OpenApiParameter.QUERY,
            description='Фильтр по проекту(возвращает все обьекты, который принадлежат одному проекту)'
        ),
    ],
)
class EstateListAPIView(CustomListAPIView):
    queryset = Estate.objects.select_related('city', 'project').all()
    serializer_class = EstateSerializer
    response_key = 'estates'
    pagination_class = LimitOffsetCustomPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['project__name', 'project__location', 'project__developer', 'description', ]
    filterset_class = EstateFilterSet


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
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ],
)
class EstateRetrieveAPIView(CustomRetrieveAPIView):
    queryset = Estate.objects.select_related('project').prefetch_related('project__facilities').all()
    serializer_class = EstateRetrieveSerializer
    lookup_field = 'id'
    response_key = 'estate'


@extend_schema(
    summary="Получить коллекцию изображений недвижимости по id",
    description="Класс представления class EstateImageRetrieveAPIView возвращает коллекцию изображений для одного"
                " объекта недвижимости модели Estate",
    methods=["GET"],
    tags=["Estate"],
)
# class EstateImageRetrieveAPIView(CustomRetrieveImagesAPIView):
#     serializer_class = EstateImageListSerializer
#
#     def get_queryset(self):
#         estate_id = self.kwargs.get('id')
#         queryset = EstateImage.objects.filter(estate_id=estate_id)
#         return queryset


@extend_schema(
    summary="Получить `похожие объекты`",
    description="Класс представления EstateRetrieveSimilarListAPIView возвращает коллекцию объектов недвижимости модели "
                "Estate в количестве от 0 до 9 шт. Тип объектов такой же как у сравниваемого объекта, города - любые. "
                "Возвращаются объекты схожие по цене.\n\n"
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
            description='Язык, на котором должны возвращаться данные (en, ar, tr, ru).'
        ),
    ],
)
class EstateRetrieveSimilarListAPIView(CustomListAPIView):
    queryset = Estate.objects.select_related('city', 'estate_type', 'project').all()
    serializer_class = EstateSerializer
    response_key = 'estates'

    def get_object(self):
        estate_id = self.kwargs.get('id')
        return Estate.objects.select_related('city', 'estate_type').get(id=estate_id)

    def filter_queryset(self, queryset):
        estate = self.get_object()
        similar: list = (Estate.objects.select_related('city', 'estate_type').
                         filter(estate_type=estate.estate_type)).order_by('price_usd')

        if len(similar) >= 11:
            index = list(similar).index(estate)
            queryset = ((similar[index - 6: index - 1] if len(similar[:index]) >= 6 else similar[:index - 1])
                        + (similar[index + 1: index + 5] if len(similar[index:]) >= 5 else similar[index + 1:]))
            return queryset

        return similar.exclude(pk=estate.id)


# _______________________ TEMPORARY _____________________________

class DataBaseAddEstateAPIView(CustomEstateCreateAPIView):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeSerializer
