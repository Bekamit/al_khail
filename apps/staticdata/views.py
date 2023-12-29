from rest_framework import generics
from .models import StaticData
from .serializers import StaticDataSerializer


class StaticDataView(generics.RetrieveUpdateAPIView):
    queryset = StaticData.objects.all()
    serializer_class = StaticDataSerializer
