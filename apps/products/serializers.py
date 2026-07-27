from rest_framework import serializers
from rest_framework.validators import ValidationError
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


class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 
            'slug',
            'icon',
            'image',
            'order'
        ]

    def validate_name(self, value):
        if 'mol' in value:
            raise ValidationError(f"{value} so'zini ishlatib bo'lmaydi")
        return value
    
    def validate_order(self, value):
        if value < 0:
            raise ValidationError("Order o dan kichik bo'lishi mumkin emas")
        return value

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