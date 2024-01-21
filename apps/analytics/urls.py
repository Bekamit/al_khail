from django.urls import path
from .views import *

urlpatterns = [
    path('analytics/', AnalyticsAPIView.as_view()),
]
