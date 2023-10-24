from django.db import models

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mercado.models import Fruta
from mercado.serializers.fruta import FrutaSerializer

class FrutaViewSet(ModelViewSet):
    queryset = Fruta.objects.all()
    serializer_class = FrutaSerializer