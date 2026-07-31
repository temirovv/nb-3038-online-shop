from rest_framework.routers import DefaultRouter
from .views import (
    BannerModelViewSet, CategoryReadOnlyModelViewSet,
    BrandReadOnlyModelViewSet, ProductReadOnlyModelViewSet)


router = DefaultRouter()
router.register(r'banners', BannerModelViewSet, basename='banner')
router.register(r'categories', CategoryReadOnlyModelViewSet, basename='category')
router.register(r'brands', BrandReadOnlyModelViewSet, basename='brand')
router.register(r'products', ProductReadOnlyModelViewSet, basename='product')

urlpatterns = router.urls
