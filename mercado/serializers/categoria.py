from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
