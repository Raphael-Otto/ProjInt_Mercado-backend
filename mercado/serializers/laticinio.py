from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Laticínio

class LaticínioSerializer(ModelSerializer):
    class Meta:
        model = Laticínio
        fields = "__all__"
        depth = 1