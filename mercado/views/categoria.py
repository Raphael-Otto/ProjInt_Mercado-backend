from django.db import models

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mercado.models import Categoria
from mercado.serializers.categoria import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]