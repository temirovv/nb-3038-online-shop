from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters

from .models import Banner, Category, Brand, Product
from .serializers import (
    BannerSerializer, CategorySerializer, 
    BrandSerializer, AddCategorySerializer,
    Productserializer)


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


class ProductReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = (
        Product.objects.filter(is_active=True)
        .select_related("category", "brand")
        .prefetch_related("images")
    )
    # N+1 problem solve
    serializer_class = Productserializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['-created_at']
    search_fields = ['name', 'brand__name']


    @action(detail=False, methods=['get'])
    def featured(self, request):
        queryset = self.get_queryset().filter(is_featured=True)
        s = self.get_serializer(queryset, many=True)
        return Response(s.data)