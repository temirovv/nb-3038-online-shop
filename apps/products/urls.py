from rest_framework.routers import DefaultRouter
from .views import BannerModelViewSet


router = DefaultRouter()
router.register(r'banners', BannerModelViewSet)

urlpatterns = router.urls
