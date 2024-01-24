from django.urls import path
from .views import *

urlpatterns = [
    path('download-catalog/', DownloadCatalogAPIView.as_view()),
]
