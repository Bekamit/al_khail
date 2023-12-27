from rest_framework.generics import CreateAPIView
from .models import Appeal
from .serializers import AppealSellValidateSerializer, AppealBuyValidateSerializer


class AppealBuyCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealBuyValidateSerializer


class AppealSellCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSellValidateSerializer
