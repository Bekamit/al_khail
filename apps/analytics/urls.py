from django.urls import path
from .views import *

urlpatterns = [
    path('catalog-download/', CatalogDownloaderCreateAPIView.as_view(model='CatalogDownloader'), name='catalog-downloader'),

    path('appeal/buy/', AppealBuyCreateAPIView.as_view(model='Appeal'), name='appeal-buy'),
    path('appeal/sell/', AppealSellCreateAPIView.as_view(model='Appeal'), name='appeal-sell'),

    path('consultation/', ConsultationCreateAPIView.as_view(model='Consultation'), name='consultation'),
]

