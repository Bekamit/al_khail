from django.urls import path
from .views import *

urlpatterns = [
    path('static_data/all/', AllStaticDataAPIView.as_view()),
    path('static_data/header/', HeaderAPIView.as_view()),
    path('static_data/body/', BodyAPIView.as_view()),
    path('static_data/forms/', FormsAPIView.as_view()),
    path('static_data/footer/', FooterAPIView.as_view()),
]
