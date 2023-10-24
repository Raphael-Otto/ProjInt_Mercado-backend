from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Bebida

class BebidaSerializer(ModelSerializer):
    class Meta:
        model = Bebida
        fields = "__all__"
        depth = 1