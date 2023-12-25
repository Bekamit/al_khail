from django.urls import path
from .views import *

urlpatterns = [
    path('estate/', EstateListAPIView.as_view()),
    path('estate/add/', EstateCreateAPIView.as_view()),
    path('estate/<int:id>/', EstateRetrieveAPIView.as_view()),
    path('estate/<int:id>/edit/', EstateRetrieveUpdateDestroyAPIView.as_view()),

    path('estate_type/', EstateTypeListAPIView.as_view()),
    path('estate_type/add/', EstateTypeCreateAPIView.as_view()),
]
