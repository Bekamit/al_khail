from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
import debug_toolbar
from core.settings import base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/redoc/", SpectacularRedocView.as_view(), name="redoc"),
    path("api/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # Third apps
    path('__debug__/', include(debug_toolbar.urls)),
    # Views
    path("api/v1/", include("apps.city.urls")),
    path("api/v1/", include("apps.company.urls")),
    path("api/v1/", include("apps.estate.urls")),
    path("api/v1/", include("apps.staticdata.urls")),
    path("api/v1/", include("apps.analytics.urls")),
]

if base.DEBUG:
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
    urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
