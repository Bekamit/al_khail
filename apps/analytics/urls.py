from django.urls import path
from .views import *

urlpatterns = [
    path('appeal/download_catalog/', CatalogDownloaderMultiSerializerListCreateAPIView.as_view()),

    path('appeal/buy/', AppealBuyCreateAPIView.as_view()),
    path('appeal/sell/', AppealSellMultiSerializerListCreateAPIView.as_view()),
]
