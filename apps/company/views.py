from service.views import CustomListAPIView

from .serializers import CompanySerializer
from .models import Company


class AboutCompanyListAPIView(CustomListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    response_key = 'about_company'
