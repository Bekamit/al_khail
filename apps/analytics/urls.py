from django.urls import path
from .views import *

urlpatterns = [
    path('catalog-download/', CatalogDownloaderMultiSerializerListCreateAPIView.as_view(), name='catalog-downloader'),

    path('appeal/buy/', AppealBuyMultiSerializerListCreateAPIView.as_view(), name='appeal-buy'),
    path('appeal/sell/', AppealSellMultiSerializerListCreateAPIView.as_view(), name='appeal-sell'),

    path('consultation/', ConsultationMultiSerializerListCreateAPIView.as_view(), name='consultation'),
]

