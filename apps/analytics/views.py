from rest_framework.generics import CreateAPIView
from apps.analytics.models import Analytics, Role
from .serializers import AnalyticsSerializer, RoleSerializer


class RoleAPIView(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)


class AnalyticsAPIView(CreateAPIView):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
