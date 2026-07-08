from rest_framework import serializers
from .models import Banner


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
