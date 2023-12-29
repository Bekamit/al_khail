from django.urls import path
from .views import *

urlpatterns = [
    path('company/', AboutCompanyListAPIView.as_view()),
#     path('company/add/', AboutCompanyCreateAPIView.as_view()),
]