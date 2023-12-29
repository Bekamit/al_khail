from django.urls import path
from .views import *

urlpatterns = [
    path('cities/', CityListAPIView.as_view()),
    # path('cities/add/', CityCreateAPIView.as_view()),
    # path('cities/<int:id>/', CityRetrieveAPIView.as_view()),
    # path('cities/<int:id>/edit/', CityRetrieveUpdateDestroyAPIView.as_view()),
]
