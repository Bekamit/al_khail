from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/redoc/", SpectacularRedocView.as_view(), name="redoc"),
    path("api/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # Views
<<<<<<< HEAD:Core/Core/urls.py
    # path("api/v1/", include("appeal.urls")),
=======
    path("api/v1/appeal/", include("appeal.urls")),
>>>>>>> 4e5b5cc (appeal):config/urls.py
    path("api/v1/", include("city.urls")),
    path("api/v1/", include("company.urls")),
    path("api/v1/", include("estate.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

