from django.urls import path
from .views import *

urlpatterns = [
    path('appeal/buy/', AppealBuyCreateAPIView.as_view()),
    path('appeal/sell/', AppealSellCreateAPIView.as_view()),
]
