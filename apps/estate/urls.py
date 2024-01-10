from django.urls import path
from .views import *

urlpatterns = [
    path('estate/', EstateListAPIView.as_view()),
    path('estate/<int:id>/', EstateRetrieveAPIView.as_view()),
    path('estate/<int:id>/images/', EstateImageRetrieveAPIView.as_view()),

    path('estate_types/', EstateTypeListAPIView.as_view()),
]
