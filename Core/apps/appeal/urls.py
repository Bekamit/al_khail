from django.urls import path
from .views import *

urlpatterns = [
    path('appeals/', AppealAPIView.as_view({'get': 'list'})),
]
