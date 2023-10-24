from django.db import models

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mercado.models import Bebida
from mercado.serializers.bebida import BebidaSerializer

class BebidaViewSet(ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer