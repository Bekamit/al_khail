from django.urls import path
from .views import *

urlpatterns = [
    path('appeals/', AppealListAPIView.as_view()),
    path('appeal/create/', AppealCreateAPIView.as_view()),
]
