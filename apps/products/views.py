from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Banner
from .serializers import BannerSerializer


class BannerModelViewSet(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = [AllowAny]
