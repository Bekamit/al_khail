from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.generics import CreateAPIView

from .models import Appeal
from .serializers import AppealSellValidateSerializer, AppealBuyValidateSerializer


@extend_schema(
    summary="Отправить запрос на покупку объекта недвижимости",
    description="Класс представления AppealBuyCreateAPIView получает данные с формы о покупке объекта недвижимости ",
    methods=["POST"],
    tags=["Appeal"],
)
class AppealBuyCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealBuyValidateSerializer


@extend_schema(
    summary="Отправить запрос на продажу объекта недвижимости",
    description="Класс представления AppealSellCreateAPIView получает данные с формы о желании клиента"
                " продать свой объект недвижимости",
    methods=["POST"],
    tags=["Appeal"],
)
class AppealSellCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSellValidateSerializer
