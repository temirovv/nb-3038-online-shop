from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Banner, Category, Brand
from .serializers import (
    BannerSerializer, CategorySerializer, 
    BrandSerializer, AddCategorySerializer)


class BannerModelViewSet(ReadOnlyModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.filter(is_active=True)
    permission_classes = [AllowAny]


class CategoryReadOnlyModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['create']:
            return AddCategorySerializer
        return self.serializer_class


class BrandReadOnlyModelViewSet(ReadOnlyModelViewSet):
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Brand.objects.filter(is_active=True).annotate(
                products_count=Count('products')
            )        
        )

    @action(detail=False, methods=['get'])
    def featured(self, request):
        queryset = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)
