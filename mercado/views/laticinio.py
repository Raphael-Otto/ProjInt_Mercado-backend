from django.db import models

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mercado.models import Laticínio
from mercado.serializers.laticinio import LaticínioSerializer

class LaticínioViewSet(ModelViewSet):
    queryset = Laticínio.objects.all()
    serializer_class = LaticínioSerializer
    