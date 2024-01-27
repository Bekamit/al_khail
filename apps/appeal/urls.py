from django.urls import path
from ..analytics.views import AppealBuyCreateAPIView, AppealSellCreateAPIView

urlpatterns = [
    path('appeal/buy/', AppealBuyCreateAPIView.as_view()),
    path('appeal/sell/', AppealSellCreateAPIView.as_view()),
]
