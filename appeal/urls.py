from .views import AppealAPIView, AppealTypeAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('type', AppealTypeAPIView)
router.register('', AppealAPIView)

urlpatterns = []
urlpatterns.extend(router.urls)
