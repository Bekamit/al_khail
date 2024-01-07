from django.urls import path
from .views import StaticDataListAPIView

urlpatterns = [
    path('staticdata/', StaticDataListAPIView.as_view()),
]
