from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Count

from .models import Banner, Category, Brand
from .serializers import BannerSerializer, CategorySerializer, BrandSerializer


class BannerModelViewSet(ReadOnlyModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.filter(is_active=True)
    permission_classes = [AllowAny]


class CategoryReadOnlyModelViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
    permission_classes = [AllowAny]


class BrandReadOnlyModelViewSet(ReadOnlyModelViewSet):
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Brand.objects.filter(is_active=True).annotate(
                products_count=Count('products')
            )        
        )
