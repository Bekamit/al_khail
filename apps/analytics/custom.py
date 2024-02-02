from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import DownloadCatalog, CatalogDownloader, Consultation
from .serializers import DownloadCatalogSerializer, CatalogDownloaderSerializer, ConsultationSerializer
from apps.staticdata.models import Form


class CustomListCreateAPIView(ListCreateAPIView):
    def get_static_form_data(self):
        try:
            form_instance = Form.get_solo()
            form_data = {
                'callback_form_title': form_instance.callback_form_title,
                'sell_form_title': form_instance.sell_form_title,
                'download_catalog_form_title': form_instance.download_catalog_form_title,
                'form_description': form_instance.form_description,
                'sell_form_description': form_instance.sell_form_description,
                'your_name': form_instance.your_name,
                'your_email': form_instance.your_email,
                'your_phone': form_instance.your_phone,
                'your_city': form_instance.your_city,
                'at_date': form_instance.at_date,
                'send': form_instance.send,
                'role': form_instance.role,
                'agent': form_instance.agent,
                'buyer': form_instance.buyer,
                'exploring': form_instance.exploring,
                'download': form_instance.download,
            }
            return form_data
        except Exception as e:
            print(f"Ошибка: {str(e)}")
            return {}

    def get(self, request, *args, **kwargs):
        form_data = self.get_static_form_data()
        return Response(form_data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if self.model == 'DownloadCatalog':
            return DownloadCatalogSerializer
        elif self.model == 'CatalogDownloader':
            return CatalogDownloaderSerializer
        elif self.model == 'Consultation':
            return ConsultationSerializer
        return None

    def get_queryset(self):
        if self.model == 'DownloadCatalog':
            return DownloadCatalog.objects.all()
        elif self.model == 'CatalogDownloader':
            return CatalogDownloader.objects.all()
        elif self.model == 'Consultation':
            return Consultation.objects.all()
        return None

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Успешно создано"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
