from django.db import models

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mercado.models import Verdura
from mercado.serializers.verdura import VerduraSerializer

class VerduraViewSet(ModelViewSet):
    queryset = Verdura.objects.all()
    serializer_class = VerduraSerializer