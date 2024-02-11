from django.urls import path
from .views import *

urlpatterns = [
    path('appeal/download_catalog/', CatalogDownloaderMultiSerializerListCreateAPIView.as_view()),

    path('appeal/buy/', AppealBuyMultiSerializerListCreateAPIView.as_view(), name='appeal-buy'),
    path('appeal/sell/', AppealSellMultiSerializerListCreateAPIView.as_view(), name='appeal-sell'),
    path('appeal/consultation/', ConsultationMultiSerializerListCreateAPIView.as_view(), name='consultation'),
]
