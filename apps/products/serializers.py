from rest_framework import serializers
from .models import Banner, Category, Brand


class BannerSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta: 
        model = Banner
        fields = [
            'title',
            'subtitle',
            'emoji',
            'gradient',
            'link',
            'logo',
            'order',
            'is_active'
        ]
    
    def get_logo(self, obj):
        request = self.request
        image = obj.image.url
        return request.build_absolute_uri(image)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name', 
            'slug',
            'icon',
            'image',
            'order'
        ]


class BrandSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    products_count = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'slug',
            'logo',
            'country',
            'description',
            'order',
            'products_count'           
        ]

    def get_logo(self, obj):
        if not obj.logo:
            return None
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(obj.logo.url)
        return obj.logo.url