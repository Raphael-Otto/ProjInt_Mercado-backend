from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Carne

class CarneSerializer(ModelSerializer):
    class Meta:
        model = Carne
        fields = "__all__"
        depth = 1
