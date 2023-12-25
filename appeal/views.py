from rest_framework import viewsets
from .models import Appeal, AppealType
from .serializers import AppealSerializer, AppealType


class AppealTypeAPIView(viewsets.ModelViewSet):
    queryset = AppealType.objects.all()
    serializer_class = AppealType


class AppealAPIView(viewsets.ModelViewSet):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
