from django.db import models

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mercado.models import Legume
from mercado.serializers.legume import LegumeSerializer

class LegumeViewSet(ModelViewSet):
    queryset = Legume.objects.all()
    serializer_class = LegumeSerializer