from django.urls import path
from .views import *

urlpatterns = [
    path('download_catalog/', CatalogDownloaderCreateAPIView.as_view()),

    path('appeal/buy/', AppealBuyCreateAPIView.as_view()),
    path('appeal/sell/', AppealSellMultiSerializerListCreateAPIView.as_view()),
]
