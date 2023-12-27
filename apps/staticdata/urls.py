from django.urls import path
from .views import StaticDataView

urlpatterns = [
    path('staticdata/<int:pk>/', StaticDataView.as_view(), name='staticdata'),
]
