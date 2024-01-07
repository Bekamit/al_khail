from drf_spectacular.utils import OpenApiParameter, extend_schema

from service.views import CustomListAPIView
from .serializers import StaticDataSerializer

from .models import StaticData


@extend_schema(
    summary="Получить статичные данные",
    description="Класс представления StaticDataListAPIView возвращает коллекцию всех статичных данных из модели SaticData "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке,"
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен"
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["StaticData"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (опционально).'
        ),
    ]
)
class StaticDataListAPIView(CustomListAPIView):
    queryset = StaticData.objects.all()
    serializer_class = StaticDataSerializer
    response_key = 'static data'
