from django.urls import path
from .views import *

urlpatterns = [
    path('download-catalog/', DownloadCatalogAPIView.as_view()),
    path('download_catalog/', CatalogDownloaderCreateAPIView.as_view()),

    path('appeal/buy/', AppealBuyCreateAPIView.as_view()),
    path('appeal/sell/', AppealSellCreateAPIView.as_view()),
]
