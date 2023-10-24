from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"