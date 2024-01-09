from rest_framework.generics import CreateAPIView
from django.utils.translation import get_language_from_request
from .models import Appeal
from .serializers import AppealSellValidateSerializer, AppealBuyValidateSerializer


class AppealBuyCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealBuyValidateSerializer

    def perform_create(self, serializer):
        lang = get_language_from_request(self.request)
        serializer.save(lang=lang)


class AppealSellCreateAPIView(CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSellValidateSerializer

    def perform_create(self, serializer):
        lang = get_language_from_request(self.request)
        serializer.save(lang=lang)
