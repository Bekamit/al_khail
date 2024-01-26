from django.urls import path
from .views import *

urlpatterns = [
    path('download_catalog/', CatalogDownloaderCreateAPIView.as_view()),
    ]

