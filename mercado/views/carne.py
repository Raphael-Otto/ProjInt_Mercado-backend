from django.db import models

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mercado.models import Carne
from mercado.serializers.carne import CarneSerializer

class CarneViewSet(ModelViewSet):
    queryset = Carne.objects.all()
    serializer_class = CarneSerializer