from drf_spectacular.utils import extend_schema, OpenApiParameter

from service.views import CustomListAPIView

from .serializers import CompanySerializer
from .models import Company


@extend_schema(
    summary="Получить блок описания `о компании`",
    description="Класс представления AboutCompanyListAPIView возвращает коллекцию из одного описания раздела 'о компании' "
                " модели Company "
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке, "
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен "
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["Company"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (опционально).'
        ),
    ],
)
class AboutCompanyListAPIView(CustomListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    response_key = 'about_company'
